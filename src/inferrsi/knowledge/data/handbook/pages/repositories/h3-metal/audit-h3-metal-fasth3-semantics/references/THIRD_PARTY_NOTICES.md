<!-- handbook
{
  "id": "repositories/h3-metal/audit-h3-metal-fasth3-semantics/references/third_party_notices",
  "kind": "reference",
  "tags": [
    "h3-metal",
    "FastH3",
    "MiniMax-H3",
    "apple-silicon",
    "metal",
    "qkv-layout",
    "swiglu",
    "bf16",
    "vsa",
    "sparse-attention",
    "fallback",
    "effective-configuration"
  ]
}
-->

# Third-party notices

> Recorded state `candidate` · empirical validation `not_run` · license `NO_LICENSE` · [Source](../../../../../../skill_library/repositories/h3-metal/audit-h3-metal-fasth3-semantics/references/THIRD_PARTY_NOTICES.md) · [Scope and provenance](../../../../../../skill_library/repositories/h3-metal/audit-h3-metal-fasth3-semantics/metadata.json) · [Parent reading](../lesson.md)

The rectangular Morton decoder and the dynamic symmetric int8 quantization /
Metal 4 TensorOps scheduling design in `h3_shaders.metal` are adapted from
ccv's Metal FlashAttention `NAMatMulKernel` and `NAInt8MatMulKernel`,
distributed under the following BSD-3-Clause license:

Copyright (c) 2010, Liu Liu
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
- Neither the name of the authors nor the names of its contributors may be
  used to endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
