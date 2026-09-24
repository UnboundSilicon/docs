14. Wake-Up Timer Command
=========================

Sets the wake-up timer prescaler and multiplier, which determine the
wake-up period.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 12:8
     - ``r4:r0``
     - Timer prescaler R
     - :c:func:`rfm12_set_wakeup_timer`
   * - 7:0
     - ``m7:m0``
     - Timer multiplier M
     - :c:func:`rfm12_set_wakeup_timer`

The command setter directly configures the prescaler and multiplier. The
:ref:`wakeup-timer-helper-functions` provide a period-based alternative.
Both setters and the reset function update staged configuration without
communicating with the radio. Use :c:func:`rfm12_apply_to_radio` to write
the staged settings.

The datasheet gives the wake-up period as
``T_wake-up = 1.03 * M * 2^R + 0.5`` milliseconds.
Timer enable is controlled separately by :c:func:`rfm12_set_wakeup_timer_enable`
in the Power Management Command.

.. note::

   The prescaler field supports values from 0 through 31, but the datasheet
   recommends 0 through 29 for future compatibility. The special command
   encoding ``0xFE00`` (R = 30, M = 0) is used for software reset;
   use ``rfm12_software_reset()`` for that operation.

For continual timer operation, the datasheet requires clearing and then
setting the Power Management Command's ``ew`` bit at the end of each cycle.
Because the enable setter is staged, apply the cleared setting before
staging and applying the enabled setting.

Data Types
----------

RFM12_wakeup_prescaler_t
~~~~~~~~~~~~~~~~~~~~~~~~

.. c:type:: uint8_t RFM12_wakeup_prescaler_t

   Wake-up timer exponent R, from 0 through 31, encoded in bits 12:8. The datasheet
   recommends 0 through 29. Together with multiplier M, the period is 1.03 * M * 2^R +
   0.5 milliseconds. R = 30 with M = 0 encodes the software-reset command; use
   :c:func:`rfm12_software_reset` for reset.

RFM12_wakeup_multiplier_t
~~~~~~~~~~~~~~~~~~~~~~~~~

.. c:type:: uint8_t RFM12_wakeup_multiplier_t

   Wake-up timer multiplier M, from 0 through 255, encoded in bits 7:0. This is a raw
   multiplier, not a period in milliseconds. See :c:type:`RFM12_wakeup_prescaler_t` for
   the period formula.

Command Functions
-----------------

rfm12_set_wakeup_timer()
----------------------------

.. c:function:: RFM12_result_t rfm12_set_wakeup_timer(RFM12_t *dev, RFM12_wakeup_prescaler_t prescaler, RFM12_wakeup_multiplier_t multiplier)

   Stage the raw wake-up timer prescaler and multiplier fields.

   This function configures the timer period. It does not enable the timer
   or communicate with the radio.

   :param dev: RFM12 radio instance.
   :param prescaler: Timer prescaler R, a five-bit value from 0 through 31;
                     the datasheet recommends 0 through 29.
   :param multiplier: Timer multiplier M, an eight-bit value from 0 through 255.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_wakeup_timer()
------------------------------

.. c:function:: RFM12_result_t rfm12_reset_wakeup_timer(RFM12_t *dev)

   Reset the staged Wake-Up Timer Command values to their defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.

.. _wakeup-timer-helper-functions:

Helper Functions
----------------

The period helper selects the closest representable timer period from a
request in milliseconds. Like the raw command setter, it stages the
prescaler and multiplier for a later :c:func:`rfm12_apply_to_radio`.
It performs no immediate SPI transfer.

rfm12_set_wakeup_period_ms()
--------------------------------

.. c:function:: RFM12_result_t rfm12_set_wakeup_period_ms(RFM12_t *dev, uint32_t wakeup_ms)

   Stage the closest representation of the requested wake-up period.

   The period is represented by the timer's prescaler and multiplier, so
   the resulting period may differ from the requested value. Timer enable
   remains a separate Power Management Command setting.

   :param dev: RFM12 radio instance.
   :param wakeup_ms: Requested wake-up period in milliseconds.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
