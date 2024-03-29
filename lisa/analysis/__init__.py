#! /usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
#
# Copyright (C) 2018, ARM Limited and contributors.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__all__ = []

# Import all the submodules before they are asked for by user code, since
# we need to create the *Analysis classes in order for them to be
# registered against TraceAnalysisBase
def _import_submodules():
    from lisa.utils import _import_all_submodules
    modules = _import_all_submodules(__name__, __path__)
    __all__.extend(modules)

_import_submodules()
# Avoid polluting the namespace with non-necessary names
del _import_submodules

# vim :set tabstop=4 shiftwidth=4 textwidth=80 expandtab
