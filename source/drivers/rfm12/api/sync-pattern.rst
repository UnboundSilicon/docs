8. Sync Pattern Command
========================

Sets the programmable synchronization byte used by the receiver.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7:0
     - ``b7:b0``
     - Synchronization byte
     - :c:func:`rfm12_set_sync_pattern`

The setter and reset function update staged configuration without
communicating with the radio. Use :c:func:`rfm12_apply_to_radio` to write
the staged settings.

The synchronization-pattern length is selected separately by
:c:func:`rfm12_set_sync_pattern_length` in the FIFO and Reset Mode Command.
In one-byte mode, the pattern consists of the programmable byte alone.
In two-byte mode, the fixed byte ``0x2D`` precedes the programmable byte.

Data Types
----------

RFM12_sync_pattern_t
~~~~~~~~~~~~~~~~~~~~

.. c:type:: uint8_t RFM12_sync_pattern_t

   Programmable synchronization byte, from 0x00 through 0xFF. In two-byte mode it
   follows the fixed 0x2D byte. Select the length with
   :c:func:`rfm12_set_sync_pattern_length`.

Command Functions
-----------------

rfm12_set_sync_pattern()
------------------------

.. c:function:: RFM12_result_t rfm12_set_sync_pattern(RFM12_t *dev, RFM12_sync_pattern_t pattern)

   Stage the programmable synchronization byte.

   The value configures Byte0 of the synchronization pattern. It does not
   change the fixed ``0x2D`` byte used in two-byte mode or the selected
   pattern length.

   This function does not communicate with the radio. The staged byte is
   written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :param pattern: Synchronization byte, from ``0x00`` through ``0xFF``.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_sync_pattern()
--------------------------

.. c:function:: RFM12_result_t rfm12_reset_sync_pattern(RFM12_t *dev)

   Reset the staged synchronization byte to its default value.

   This function does not communicate with the radio. The changed byte is
   written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
