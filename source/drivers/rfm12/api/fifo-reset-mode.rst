7. FIFO and Reset Mode Command
==============================

Configures FIFO filling, the FIFO interrupt level, synchronization-pattern
length, and reset sensitivity.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7:4
     - ``f3:f0``
     - FIFO interrupt level
     - :c:func:`rfm12_set_fifo_interrupt_level`
   * - 3
     - ``sp``
     - Synchronization-pattern length
     - :c:func:`rfm12_set_sync_pattern_length`
   * - 2
     - ``al``
     - FIFO fill-start condition
     - :c:func:`rfm12_set_fifo_fill_start`
   * - 1
     - ``ff``
     - FIFO fill enable
     - :c:func:`rfm12_set_rx_fifo_fill_enable`
   * - 0
     - ``dr``
     - Reset-mode sensitivity
     - :c:func:`rfm12_set_reset_mode`

The functions listed in the register field table above directly configure
fields in the FIFO and Reset Mode Command. The setters and reset function
update staged configuration without communicating with the radio. Use
:c:func:`rfm12_apply_to_radio` to write the staged settings.

The :ref:`fifo-reset-mode-helper-functions` section describes the operation
for restarting synchronization-pattern recognition. Unlike the staged
setters, this helper communicates with the radio immediately.

Command Functions
-----------------

rfm12_set_fifo_interrupt_level()
--------------------------------

.. c:function:: RFM12_result_t rfm12_set_fifo_interrupt_level(RFM12_t *dev, RFM12_fifo_interrupt_level_t level)

   Stage the FIFO interrupt level.

   The FIFO generates an interrupt when the number of received data bits
   reaches the selected level. The setter accepts values from 1 through
   15 bits.

   :param dev: RFM12 radio instance.
   :param level: FIFO interrupt threshold in bits, from 1 through 15.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_sync_pattern_length()
-------------------------------

.. c:function:: RFM12_result_t rfm12_set_sync_pattern_length(RFM12_t *dev, RFM12_sync_pattern_length_t length)

   Stage the synchronization-pattern length.

   Select ``RFM12_SYNC_PATTERN_2BYTE`` for the fixed byte ``0x2D`` followed
   by the programmable synchronization byte, or ``RFM12_SYNC_PATTERN_1BYTE``
   for the programmable byte alone. The programmable byte is configured
   by the Sync Pattern Command.

   :param dev: RFM12 radio instance.
   :param length: One-byte or two-byte synchronization-pattern selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_fifo_fill_start()
---------------------------

.. c:function:: RFM12_result_t rfm12_set_fifo_fill_start(RFM12_t *dev, RFM12_fifo_fill_start_t mode)

   Stage the condition that starts FIFO filling.

   Select ``RFM12_FIFO_FILL_AFTER_SYNC`` to start filling after recognizing
   the synchronization pattern, or ``RFM12_FIFO_FILL_ALWAYS`` to fill
   without waiting for synchronization. FIFO filling must also be enabled
   with :c:func:`rfm12_set_rx_fifo_fill_enable`.

   :param dev: RFM12 radio instance.
   :param mode: FIFO fill-start condition.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_rx_fifo_fill_enable()
-------------------------------

.. c:function:: RFM12_result_t rfm12_set_rx_fifo_fill_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the receiver FIFO fill-enable setting.

   When applied, disabling this setting stops FIFO filling. Enabling it
   permits filling according to the configured fill-start condition.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable receiver FIFO filling.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_reset_mode()
----------------------

.. c:function:: RFM12_result_t rfm12_set_reset_mode(RFM12_t *dev, RFM12_reset_mode_t mode)

   Stage the hardware reset sensitivity.

   Select ``RFM12_RESET_MODE_SENSITIVE`` for the highly sensitive reset
   mode, or ``RFM12_RESET_MODE_NON_SENSITIVE`` to disable that mode.
   This setting controls the radio's response to supply-voltage drops
   and glitches; it does not issue a reset.

   :param dev: RFM12 radio instance.
   :param mode: Reset sensitivity selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_fifo_reset_mode()
-----------------------------

.. c:function:: RFM12_result_t rfm12_reset_fifo_reset_mode(RFM12_t *dev)

   Reset the staged FIFO and Reset Mode Command values to their defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.

.. _fifo-reset-mode-helper-functions:

Helper Functions
----------------

The synchronization restart helper clears and then sets the FIFO fill-enable
bit to restart synchronization-pattern recognition. It performs two immediate
SPI transfers of the complete FIFO and Reset Mode Command.

Any pending FIFO and Reset Mode Command settings are included in these
transfers. The staged FIFO configuration stored in the driver is unchanged.

rfm12_restart_sync_recognition()
--------------------------------

.. c:function:: RFM12_result_t rfm12_restart_sync_recognition(RFM12_t *dev)

   Restart receiver synchronization-pattern recognition immediately.

   The staged FIFO fill-enable setting must already be enabled. The helper
   writes the command with ``ff`` cleared, then writes it again with ``ff``
   set. This also applies any pending settings belonging to this command
   without modifying the staged FIFO configuration.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
