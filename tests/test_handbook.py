import json
from pathlib import Path

import pytest

from inferrsi.apps.cli import main
from inferrsi.knowledge.handbook import BOOK, Handbook, markdown
from tools.check_handbook import contents
from tools.port_handbook import prepare_prose, sections


@pytest.fixture(scope="module")
def book():
    return Handbook()


def test_ported_identities_and_navigation(book):
    receipt = json.loads((BOOK / "migration.json").read_text(encoding="utf-8"))
    for path, ref in receipt["catalog_aliases"].items():
        catalog_id = json.loads((BOOK.parent / path).read_text(encoding="utf-8"))["id"]
        assert book.resolve("package:" + catalog_id) == book.resolve("checkout:" + ref)
    for name, expected in contents(book).items():
        assert (BOOK / "contents" / name).read_text(encoding="utf-8") == expected
    assert {book.pages[ref].kind for ref in receipt["converted"].values()} >= {
        "case",
        "procedure",
        "reference",
        "profile",
        "record",
    }


def test_standalone_finding_and_contributing_records_keep_evidence_limits(book):
    case = book.pages["case.qwen-ascend-rejected-directions"]
    key = next(k for k in case.sections if "eager-rope-table" in k)
    item = book.read("checkout:" + case.id + "#" + key)
    assert all(
        term in item["body"]
        for term in (
            "no_gain",
            "regime_bound",
            "910B1",
            "TORCH_SDPA",
            "locally_verified=false",
            "INCONCLUSIVE",
        )
    )
    record = book.read("mlx.mlx.execution.evaluation_completion#unit-what-the-source-reports")
    assert "locally verified `false`" in record["body"]
    assert "bff10220" in record["body"] and "No MLX backend test" in record["body"]


def test_compose_and_follow_links_at_section_granularity(book):
    section = "measurement-boundaries#unit-completion"
    items = book.compose(["test-a-speedup", section])
    refs = [item["ref"] for item in items]
    assert refs[0] == "conditional-bounds#unit-floor" and refs.count(section) == 1
    assert refs[-1] == "rsi-evidence#unit-verdicts"
    assert {"relation": "includes", "ref": "test-a-speedup#unit-readings"} in (
        book.links(section)["incoming"]
    )
    result = markdown(items)
    assert "](pages/records/dependency/mlx/mlx/execution/evaluation-completion.md#" in result
    parent = book.links("performance-ceiling-analysis#unit-three-level-ceiling-model")
    assert any("flexgen-offload-feasibility" in edge["ref"] for edge in parent["outgoing"])


def test_cli_search_and_guarded_read(capsys, book):
    args = ["knowledge", "handbook"]
    assert (
        main([*args, "search", "admission drain", "--kind", "case", "--limit", "4", "--json"]) == 0
    )
    results = json.loads(capsys.readouterr().out)
    assert any("case.admission-drain-occupancy#unit-" in item["ref"] for item in results)
    ref = results[0]["ref"]
    assert main([*args, "read", ref, "--revision", results[0]["revision"], "--json"]) == 0
    assert json.loads(capsys.readouterr().out) == book.read(ref)
    with pytest.raises(SystemExit) as error:
        main([*args, "read", ref, "--revision", "old"])
    assert error.value.code == 2
    assert book.read("../" + results[0]["path"])["ref"] == ref.partition("#")[0]
    assert book.search("unknown-term-zzzzzz", under="no-such-chapter") == []


def write_page(root: Path, name: str, body: str, **meta):
    page = root / "pages" / (name + ".md")
    page.parent.mkdir(exist_ok=True)
    header = json.dumps({"id": name, "kind": "concept", **meta})
    page.write_text(f"<!-- handbook\n{header}\n-->\n\n# Title\n\n{body}\n", encoding="utf-8")


def test_revision_tracks_the_selected_text_and_shared_context(tmp_path):
    first = '<a id="unit-first"></a>\n## Measurement\n\nOriginal'
    second = '<a id="unit-other"></a>\n## Other\n\n'
    limits = '<a id="unit-limits"></a>\n## Limits\n\nOne cohort'
    meta = {"carry": ["unit-limits"]}
    write_page(tmp_path, "test", "\n\n".join([first, second + "Initial", limits]), **meta)
    ref = "test#unit-first"
    revision = Handbook(tmp_path).read(ref)["revision"]
    write_page(tmp_path, "test", "\n\n".join([first, second + "Edited", limits]), **meta)
    assert Handbook(tmp_path).read(ref, revision)["revision"] == revision
    write_page(tmp_path, "test", "\n\n".join([first, second, limits + " changed"]), **meta)
    with pytest.raises(ValueError, match="Revision mismatch"):
        Handbook(tmp_path).read(ref, revision)


@pytest.mark.parametrize(
    ("target", "error"),
    [
        ("x.md", "cycle"),
        ("missing.md", "Broken handbook"),
        ("x.md#typo", "Missing section"),
    ],
)
def test_invalid_reading_path_cannot_produce_a_partial_composition(tmp_path, target, error):
    write_page(
        tmp_path, "x", f'<a id="unit-readings"></a>\n## Read\n\n1. [Step]({target})', kind="path"
    )
    with pytest.raises(ValueError, match=error):
        Handbook(tmp_path).compose(["x"])


def test_port_resolves_reference_citations_and_respects_nested_documents_and_code():
    source = (
        "# Second paper\n\n## Evidence\n\nSee [trial][A].\n\n"
        "````md\n# A literal heading\n```\n[trial][A]\n````\n\n[A]: facts.json"
    )
    converted = sections(prepare_prose(source))
    assert '<a id="unit-second-paper"></a>\n## Second paper' in converted
    assert '<a id="unit-evidence"></a>\n### Evidence' in converted
    assert "See [trial](facts.json)." in converted
    assert "````md\n# A literal heading\n```\n[trial][A]\n````" in converted
