9. Receiver FIFO Read Command
=============================

Reads one received byte from the receiver FIFO.

Register Fields
---------------

Unlike the configuration commands, the Receiver FIFO Read Command has no configurable fields. The transmitted byte is fixed, and the received byte contains the FIFO data.

.. list-table::
   :header-rows: 1

   * - Direction
     - Bits
     - Meaning
     - API
   * - TX
     - 7:0
     - Fixed command value (``0x00``)
     - —
   * - RX
     - 7:0
     - Received FIFO data
     - :c:func:`rfm12_read_fifo`

This command performs an immediate SPI transfer. It transmits ``0xB000``
and returns the low eight bits of the response as the received byte.
It does not require :c:func:`rfm12_apply_to_radio` to perform the read.

Receiver FIFO mode must already be enabled through the ``ef`` bit in the
Configuration Setting Command. Use ``rfm12_set_rx_fifo_mode_enable()``
and apply that staged setting before reading the FIFO.

During FIFO access, the SPI clock frequency must not exceed one quarter
of the crystal oscillator frequency. If the SPI clock duty cycle is not
50 percent, the shorter clock pulse must last at least two crystal
oscillator periods.

Command Functions
-----------------

rfm12_read_fifo()
-----------------

.. c:function:: RFM12_result_t rfm12_read_fifo(RFM12_t *dev, uint8_t *data)

   Read one byte from the receiver FIFO immediately.

   This function communicates with the radio through the configured SPI
   callback and returns the received FIFO byte through ``data``.

   :param dev: RFM12 radio instance.
   :param data: Receives the byte read from the receiver FIFO.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
