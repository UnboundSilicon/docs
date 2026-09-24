6. Data Filter Command
======================

Configures clock recovery, data filtering, and the Data Quality Detector
(DQD) threshold.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7
     - ``al``
     - Automatic clock-recovery mode
     - :c:func:`rfm12_set_clock_recovery_mode`
   * - 6
     - ``ml``
     - Manual clock-recovery speed
     - :c:func:`rfm12_set_clock_recovery_speed`
   * - 5
     - Fixed
     - Must be ``1``
     - None
   * - 4
     - ``s``
     - Filter type
     - :c:func:`rfm12_set_filter_type`
   * - 3
     - Fixed
     - Must be ``1``
     - None
   * - 2:0
     - ``f2:f0``
     - Data Quality Detector threshold
     - :c:func:`rfm12_set_dqd_threshold`

The setters listed in the register field table above directly configure
fields in the Data Filter Command. The setters and reset function update
staged configuration without communicating with the radio. Use
:c:func:`rfm12_apply_to_radio` to write the staged settings.

Data Types
----------

RFM12_clock_recovery_mode_t
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_clock_recovery_mode_t

   Enum. Automatic or manual clock recovery selection for bit 7.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_CLOCK_RECOVERY_MANUAL``
        - ``0``
        - Manual speed selection.
      * - ``RFM12_CLOCK_RECOVERY_AUTO``
        - ``1``
        - Automatic clock recovery.


RFM12_clock_recovery_speed_t
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_clock_recovery_speed_t

   Enum. Manual clock recovery speed for bit 6. Used only with
   RFM12_CLOCK_RECOVERY_MANUAL.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_CLOCK_RECOVERY_SLOW``
        - ``0``
        - Slow recovery.
      * - ``RFM12_CLOCK_RECOVERY_FAST``
        - ``1``
        - Fast recovery.


RFM12_filter_type_t
~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_filter_type_t

   Enum. Receive data filter selection for bit 4.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_FILTER_DIGITAL``
        - ``0``
        - Digital filter.
      * - ``RFM12_FILTER_ANALOG_RC``
        - ``1``
        - Analog RC filter.


RFM12_dqd_threshold_t
~~~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_dqd_threshold_t

   Enum. Data Quality Detector threshold for bits 2:0. Hardware supports 0 through 7;
   the recommended operating range is 5 through 7.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_DQD_THRESHOLD_0``
        - ``0``
        - Threshold 0.
      * - ``RFM12_DQD_THRESHOLD_1``
        - ``1``
        - Threshold 1.
      * - ``RFM12_DQD_THRESHOLD_2``
        - ``2``
        - Threshold 2.
      * - ``RFM12_DQD_THRESHOLD_3``
        - ``3``
        - Threshold 3.
      * - ``RFM12_DQD_THRESHOLD_4``
        - ``4``
        - Threshold 4.
      * - ``RFM12_DQD_THRESHOLD_5``
        - ``5``
        - Threshold 5.
      * - ``RFM12_DQD_THRESHOLD_6``
        - ``6``
        - Threshold 6.
      * - ``RFM12_DQD_THRESHOLD_7``
        - ``7``
        - Threshold 7.

Command Functions
-----------------

rfm12_set_clock_recovery_mode()
-------------------------------

.. c:function:: RFM12_result_t rfm12_set_clock_recovery_mode(RFM12_t *dev, RFM12_clock_recovery_mode_t mode)

   Stage the clock-recovery mode.

   Select ``RFM12_CLOCK_RECOVERY_AUTO`` to start clock recovery in fast mode
   and switch to slow mode after locking. In automatic mode, the manual
   speed setting has no effect.

   Select ``RFM12_CLOCK_RECOVERY_MANUAL`` to use the speed selected by
   :c:func:`rfm12_set_clock_recovery_speed`.

   :param dev: RFM12 radio instance.
   :param mode: Automatic or manual clock-recovery mode.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_clock_recovery_speed()
--------------------------------

.. c:function:: RFM12_result_t rfm12_set_clock_recovery_speed(RFM12_t *dev, RFM12_clock_recovery_speed_t speed)

   Stage the manual clock-recovery speed.

   Select ``RFM12_CLOCK_RECOVERY_FAST`` for fast attack and release, or
   ``RFM12_CLOCK_RECOVERY_SLOW`` for slow attack and release. This setting
   takes effect only when clock recovery is in manual mode.

   The datasheet recommends a 4- to 8-bit alternating preamble for fast
   mode and a 12- to 16-bit preamble for slow mode. Slow mode requires
   more accurate bit timing.

   :param dev: RFM12 radio instance.
   :param speed: Manual clock-recovery speed selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_filter_type()
-----------------------

.. c:function:: RFM12_result_t rfm12_set_filter_type(RFM12_t *dev, RFM12_filter_type_t filter_type)

   Stage the data-filter type.

   Select ``RFM12_FILTER_DIGITAL`` for the digital filter, whose time
   constant is automatically adjusted to the data rate configured by
   :c:func:`rfm12_set_data_rate`.

   Select ``RFM12_FILTER_ANALOG_RC`` for the analog RC filter. This mode
   requires an external capacitor between pin 7 and VSS to set the filter
   cutoff frequency. The internal clock-recovery circuit and FIFO cannot
   be used with the analog RC filter.

   :param dev: RFM12 radio instance.
   :param filter_type: Digital or analog RC filter selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_dqd_threshold()
-------------------------

.. c:function:: RFM12_result_t rfm12_set_dqd_threshold(RFM12_t *dev, RFM12_dqd_threshold_t threshold)

   Stage the Data Quality Detector threshold.

   The hardware supports thresholds 0 through 7, selected using
   ``RFM12_DQD_THRESHOLD_0`` through ``RFM12_DQD_THRESHOLD_7``.
   The datasheet recommends thresholds 5 through 7; lower thresholds can
   cause noise to be treated as a valid FSK signal.

   :param dev: RFM12 radio instance.
   :param threshold: Data Quality Detector threshold selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_data_filter()
-------------------------

.. c:function:: RFM12_result_t rfm12_reset_data_filter(RFM12_t *dev)

   Reset the staged Data Filter Command values to their defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
