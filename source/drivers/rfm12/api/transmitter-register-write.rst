13. Transmitter Register Write Command
======================================

Writes one byte to the transmitter data register.

Register Fields
---------------

The command carries a transmit data byte rather than staged configuration
settings.

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7:0
     - ``t7:t0``
     - Transmit data byte
     - :c:func:`rfm12_write_tx_register`

This command performs an immediate SPI transfer. It transmits
``0xB800 | data``, placing the data byte in the low eight bits of the
command word. It does not require :c:func:`rfm12_apply_to_radio` to
perform the write.

The TX data register must already be enabled through the ``el`` bit in the
Configuration Setting Command. Use
:c:func:`rfm12_set_tx_data_register_enable` and apply that staged setting
before writing transmit data.

Command Functions
-----------------

rfm12_write_tx_register()
----------------------------

.. c:function:: RFM12_result_t rfm12_write_tx_register(RFM12_t *dev, uint8_t data)

   Write one byte to the transmitter data register immediately.

   This function communicates with the radio through the configured SPI
   callback. The write loads the byte into the data register; it does not
   indicate that transmission of the byte over the air has completed.

   :param dev: RFM12 radio instance.
   :param data: Byte to write to the transmitter data register.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
