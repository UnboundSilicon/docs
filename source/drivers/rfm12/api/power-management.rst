2. Power Management Command
===========================

Enables and disables the radio's receiver, transmitter, and supporting
functional blocks.

The individual setters and reset function update staged configuration without
communicating with the radio. Use :c:func:`rfm12_apply_to_radio` to write the
staged settings. The mode helpers perform immediate SPI transfers and write
the complete Power Management Command, including any pending settings for
this command.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7
     - ``er``
     - Receiver enable
     - :c:func:`rfm12_set_receiver_enable`
   * - 6
     - ``ebb``
     - Receiver baseband enable
     - :c:func:`rfm12_set_baseband_enable`
   * - 5
     - ``et``
     - Transmitter enable
     - :c:func:`rfm12_set_transmitter_enable`
   * - 4
     - ``es``
     - Synthesizer enable
     - :c:func:`rfm12_set_synthesizer_enable`
   * - 3
     - ``ex``
     - Crystal oscillator enable
     - :c:func:`rfm12_set_crystal_oscillator_enable`
   * - 2
     - ``eb``
     - Low-battery detector enable
     - :c:func:`rfm12_set_low_battery_detector_enable`
   * - 1
     - ``ew``
     - Wake-up timer enable
     - :c:func:`rfm12_set_wakeup_timer_enable`
   * - 0
     - ``dc``
     - Clock output disable
     - :c:func:`rfm12_set_clock_output_enable`

The functions listed in the register field table above directly configure
fields in the Power Management Command. These settings are staged and are
written to the radio by :c:func:`rfm12_apply_to_radio`.

The :ref:`power-management-helper-functions` provide higher-level operations
for placing the radio into common operating modes. Unlike the staged setters,
these functions communicate with the radio immediately.

Command Functions
-----------------

rfm12_set_receiver_enable()
---------------------------

.. c:function:: RFM12_result_t rfm12_set_receiver_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the receiver enable setting.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the receiver.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_baseband_enable()
---------------------------

.. c:function:: RFM12_result_t rfm12_set_baseband_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the receiver baseband circuits enable setting.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the receiver baseband circuits.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_transmitter_enable()
------------------------------

.. c:function:: RFM12_result_t rfm12_set_transmitter_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the transmitter enable setting.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the transmitter.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_synthesizer_enable()
------------------------------

.. c:function:: RFM12_result_t rfm12_set_synthesizer_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the synthesizer enable setting.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the synthesizer.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_crystal_oscillator_enable()
-------------------------------------

.. c:function:: RFM12_result_t rfm12_set_crystal_oscillator_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the crystal oscillator enable setting.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the crystal oscillator.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_low_battery_detector_enable()
---------------------------------------

.. c:function:: RFM12_result_t rfm12_set_low_battery_detector_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the low-battery detector enable setting.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the low-battery detector.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_wakeup_timer_enable()
-------------------------------

.. c:function:: RFM12_result_t rfm12_set_wakeup_timer_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the wake-up timer enable setting.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the wake-up timer.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_clock_output_enable()
-------------------------------

.. c:function:: RFM12_result_t rfm12_set_clock_output_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the clock output enable setting.

   The hardware ``dc`` bit disables the clock output. Enabling the clock
   output clears ``dc``; disabling the clock output sets it.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the clock output.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_power_management()
------------------------------

.. c:function:: RFM12_result_t rfm12_reset_power_management(RFM12_t *dev)

   Reset the staged Power Management Command values to their defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.

.. _power-management-helper-functions:

Helper Functions
----------------

The mode helper functions provide convenient operations for placing the radio
into its defined operating modes. They perform an immediate SPI transfer of
the Power Management Command rather than staging the change for a later
:c:func:`rfm12_apply_to_radio`.

Any pending Power Management Command settings are included in that transfer.

rfm12_enter_rx_mode()
---------------------

.. c:function:: RFM12_result_t rfm12_enter_rx_mode(RFM12_t *dev)

   Enter receive mode by immediately writing the Power Management Command.

   This also applies any pending settings belonging to this command. The
   driver's tracked operating mode is updated after a successful transfer.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_enter_tx_mode()
---------------------

.. c:function:: RFM12_result_t rfm12_enter_tx_mode(RFM12_t *dev)

   Enter transmit mode by immediately writing the Power Management Command.

   This also applies any pending settings belonging to this command. The
   driver's tracked operating mode is updated after a successful transfer.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_enter_idle_mode()
-----------------------

.. c:function:: RFM12_result_t rfm12_enter_idle_mode(RFM12_t *dev)

   Enter idle mode by immediately writing the Power Management Command.

   This also applies any pending settings belonging to this command. The
   driver's tracked operating mode is updated after a successful transfer.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_enter_standby_mode()
--------------------------

.. c:function:: RFM12_result_t rfm12_enter_standby_mode(RFM12_t *dev)

   Enter standby mode by immediately writing the Power Management Command.

   This also applies any pending settings belonging to this command. The
   driver's tracked operating mode is updated after a successful transfer.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_enter_sleep_mode()
------------------------

.. c:function:: RFM12_result_t rfm12_enter_sleep_mode(RFM12_t *dev)

   Enter sleep mode by immediately writing the Power Management Command.

   This also applies any pending settings belonging to this command. The
   driver's tracked operating mode is updated after a successful transfer.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
