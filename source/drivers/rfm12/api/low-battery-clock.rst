16. Low Battery Detector and Microcontroller Clock Divider Command
==================================================================

Sets the low-battery detector threshold and microcontroller clock-output
frequency.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7:5
     - ``d2:d0``
     - Clock-output frequency
     - :c:func:`rfm12_set_clock_output_frequency`
   * - 4
     - Fixed
     - Must be ``0``
     - None
   * - 3:0
     - ``v3:v0``
     - Low-battery threshold
     - :c:func:`rfm12_set_low_battery_threshold`

The setters listed in the register field table above directly configure
fields in the Low Battery Detector and Microcontroller Clock Divider
Command. The setters and reset function update staged configuration without
communicating with the radio. Use :c:func:`rfm12_apply_to_radio` to write
the staged settings.

The detector and clock output are enabled separately through
:c:func:`rfm12_set_low_battery_detector_enable` and
:c:func:`rfm12_set_clock_output_enable` in the Power Management Command.
The hardware ``eb`` bit enables the detector, while ``dc`` disables the
clock output; the clock-output enable API handles this inverted polarity.

Command Functions
-----------------

rfm12_set_clock_output_frequency()
--------------------------------------

.. c:function:: RFM12_result_t rfm12_set_clock_output_frequency(RFM12_t *dev, RFM12_clock_output_frequency_t frequency)

   Stage the microcontroller clock-output frequency.

   .. list-table::
      :header-rows: 1

      * - Selection
        - ``d2:d0``
        - Clock-output frequency
      * - ``RFM12_CLOCK_OUTPUT_1MHZ``
        - ``000``
        - 1 MHz
      * - ``RFM12_CLOCK_OUTPUT_1_25MHZ``
        - ``001``
        - 1.25 MHz
      * - ``RFM12_CLOCK_OUTPUT_1_66MHZ``
        - ``010``
        - 1.66 MHz
      * - ``RFM12_CLOCK_OUTPUT_2MHZ``
        - ``011``
        - 2 MHz
      * - ``RFM12_CLOCK_OUTPUT_2_5MHZ``
        - ``100``
        - 2.5 MHz
      * - ``RFM12_CLOCK_OUTPUT_3_33MHZ``
        - ``101``
        - 3.33 MHz
      * - ``RFM12_CLOCK_OUTPUT_5MHZ``
        - ``110``
        - 5 MHz
      * - ``RFM12_CLOCK_OUTPUT_10MHZ``
        - ``111``
        - 10 MHz

   This selects the clock division ratio. The CLK output-buffer drive
   current is configured separately by
   :c:func:`rfm12_set_pll_output_buffer_current`.

   :param dev: RFM12 radio instance.
   :param frequency: Predefined clock-output frequency selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_low_battery_threshold()
-------------------------------------

.. c:function:: RFM12_result_t rfm12_set_low_battery_threshold(RFM12_t *dev, RFM12_low_battery_threshold_t threshold)

   Stage the low-battery detector threshold voltage.

   Select a predefined threshold from
   ``RFM12_LOW_BATTERY_THRESHOLD_2_25V`` through
   ``RFM12_LOW_BATTERY_THRESHOLD_3_75V`` in 0.10 V increments.
   Pass the enum constant rather than a numeric voltage.

   The threshold is ``V_LB = 2.25 V + V * 0.10 V``, where ``V`` is the
   four-bit ``v3:v0`` field. This setter does not enable the detector;
   use :c:func:`rfm12_set_low_battery_detector_enable` for that setting.

   :param dev: RFM12 radio instance.
   :param threshold: Predefined low-battery threshold selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_low_battery_clock()
-----------------------------------

.. c:function:: RFM12_result_t rfm12_reset_low_battery_clock(RFM12_t *dev)

   Reset the staged low-battery threshold and clock-divider settings to
   their defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
