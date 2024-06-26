# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Abstract traffic handler."""

import abc
from typing import Any, Mapping

from load_test.data import data_loader as abstract_data_loader
from load_test.targets import target as abstract_target


class TrafficHandler(abc.ABC):
  """Base abstraction for traffic handlers."""

  def __init__(
      self,
      target: abstract_target.Target,
      data_loader: abstract_data_loader.DataLoader):
    self.target = target
    self.data_loader = data_loader

  @abc.abstractmethod
  def start(self):
    """Starts the load test."""
    pass

  @property
  @abc.abstractmethod
  def metrics(self) -> Mapping[str, Any]:
    """Metrics generated by the handler."""
    raise NotImplementedError()
