15. Low Duty-Cycle Command
==========================

Configures periodic receiver operation to reduce average power consumption.
The receiver wakes briefly to check for an FSK transmission and extends its
on-time while the Data Quality Detector (DQD) indicates a good signal.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7:1
     - ``d6:d0``
     - Duty-cycle parameter D
     - :c:func:`rfm12_set_low_duty_cycle_d`
   * - 0
     - ``en``
     - Low duty-cycle enable
     - :c:func:`rfm12_set_low_duty_cycle_enable`

The setters listed in the register field table above directly configure
fields in the Low Duty-Cycle Command. The setters and reset function update
staged configuration without communicating with the radio. Use
:c:func:`rfm12_apply_to_radio` to write the staged settings.

The Wake-Up Timer Command determines the cycle period. The nominal duty
cycle is ``(2 * D + 1) / M * 100%``, where ``M`` is the wake-up timer
multiplier configured by :c:func:`rfm12_set_wakeup_timer`. This calculation
requires a nonzero multiplier.

.. note::

   Low duty-cycle operation requires ``er`` to be cleared and ``ew`` to be
   set in the Power Management Command. Stage these settings with
   :c:func:`rfm12_set_receiver_enable` and
   :c:func:`rfm12_set_wakeup_timer_enable`, respectively, and apply them
   along with the duty-cycle configuration. The radio does not generate
   wake-up timer interrupts in this mode.

Allow enough receiver on-time for the crystal oscillator, synthesizer, and
PLL to start and for DQD to recognize valid data. An on-time that is too
short can prevent reception even when the incoming signal is good.

Command Functions
-----------------

rfm12_set_low_duty_cycle_d()
--------------------------------

.. c:function:: RFM12_result_t rfm12_set_low_duty_cycle_d(RFM12_t *dev, RFM12_low_duty_cycle_d_t d)

   Stage the low duty-cycle parameter D.

   The setter accepts values from 0 through 127. Pass the raw D field,
   not a percentage; the resulting duty cycle also depends on the wake-up
   timer multiplier M.

   :param dev: RFM12 radio instance.
   :param d: Duty-cycle parameter D, from 0 through 127.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_low_duty_cycle_enable()
------------------------------------

.. c:function:: RFM12_result_t rfm12_set_low_duty_cycle_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the low duty-cycle enable setting.

   The wake-up timer and Power Management Command settings must also be
   configured for periodic receiver operation as described above.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable low duty-cycle operation.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_low_duty_cycle()
--------------------------------

.. c:function:: RFM12_result_t rfm12_reset_low_duty_cycle(RFM12_t *dev)

   Reset the staged Low Duty-Cycle Command values to their defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
