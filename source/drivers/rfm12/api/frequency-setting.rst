3. Frequency Setting Command
============================

The frequency API configures the RFM12 carrier frequency.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 11:0
     - ``f11:f0``
     - Frequency setting
     - :c:func:`rfm12_set_frequency`

rfm12_set_frequency()
---------------------

.. c:function:: RFM12_result_t rfm12_set_frequency(RFM12_t *dev, RFM12_frequency_hz_t frequency_hz)

   Stage the desired carrier frequency for the RFM12 radio.

   The requested frequency is normalized to the nearest frequency that can
   be represented by the RFM12 for the selected frequency band.

   This function does not communicate with the radio. The staged frequency
   is written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :param frequency_hz: Desired carrier frequency in Hz.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.

rfm12_get_frequency()
---------------------

.. c:function:: RFM12_result_t rfm12_get_frequency(const RFM12_t *dev, RFM12_frequency_hz_t *frequency_hz)

   Get the currently staged carrier frequency.

   :param dev: RFM12 radio instance.
   :param frequency_hz: Receives the staged carrier frequency in Hz.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_frequency()
-----------------------

.. c:function:: RFM12_result_t rfm12_reset_frequency(RFM12_t *dev)

   Reset the staged carrier frequency to its default value.

   This function does not communicate with the radio. The changed frequency
   is written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
