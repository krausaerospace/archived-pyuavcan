#
# Copyright (c) 2019 UAVCAN Development Team
# This software is distributed under the terms of the MIT License.
# Author: Pavel Kirienko <pavel.kirienko@zubax.com>
#

"""
CAN transport overview
++++++++++++++++++++++

This module implements the CAN transport for UAVCAN: both CAN 2.0 and CAN FD.
UAVCAN does not distinguish between the two aside from the MTU difference; neither does this implementation.
CAN 2.0 is essentially treated as CAN FD with MTU of 8 bytes.

Different CAN hardware is supported through the media sublayer; please refer to :mod:`pyuavcan.transport.can.media`.

Per the UAVCAN specification, the CAN transport supports broadcast messages and unicast services:

+--------------------+--------------------------+---------------------------+
| Supported transfers| Unicast                  | Broadcast                 |
+====================+==========================+===========================+
|**Message**         | No                       | Yes                       |
+--------------------+--------------------------+---------------------------+
|**Service**         | Yes                      | Banned by Specification   |
+--------------------+--------------------------+---------------------------+


Tooling
+++++++

Some of the media sub-layer implementations support virtual CAN bus interfaces
(e.g., SocketCAN on GNU/Linux); they are often useful for testing.
Please read the media sub-layer documentation for details.


Inheritance diagram
+++++++++++++++++++

.. inheritance-diagram:: pyuavcan.transport.can._can
                         pyuavcan.transport.can._session._input
                         pyuavcan.transport.can._session._output
   :parts: 1
"""

# Please keep the elements well-ordered because the order is reflected in the docs.
# Core components first.
from ._can import CANTransport as CANTransport

from ._session import CANInputSession as CANInputSession
from ._session import CANOutputSession as CANOutputSession

# Statistics.
from ._can import CANTransportStatistics as CANTransportStatistics

from ._session import CANInputSessionStatistics as CANInputSessionStatistics
from ._session import TransferReassemblyErrorID as TransferReassemblyErrorID

# Media sub-layer.
from . import media as media
