4. Data Rate Command
====================

Selects the transmitter bit rate and the expected receiver bit rate.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7
     - ``cs``
     - Data-rate scale selection
     - :c:func:`rfm12_set_data_rate`
   * - 6:0
     - ``r6:r0``
     - Data-rate parameter R
     - :c:func:`rfm12_set_data_rate`

The setter selects a predefined data rate, which the driver encodes into the
``cs`` and ``R`` fields. The setter and reset function update staged
configuration without communicating with the radio. Use
:c:func:`rfm12_apply_to_radio` to write the staged settings.

The getter returns the staged selection without reading from the radio.

Command Functions
-----------------

rfm12_set_data_rate()
---------------------

.. c:function:: RFM12_result_t rfm12_set_data_rate(RFM12_t *dev, RFM12_data_rate_t rate)

   Stage the receiver and transmitter data rate.

   Select one of the predefined rates: ``RFM12_DATA_RATE_1200``,
   ``RFM12_DATA_RATE_2400``, ``RFM12_DATA_RATE_4800``,
   ``RFM12_DATA_RATE_9600``, ``RFM12_DATA_RATE_19200``,
   ``RFM12_DATA_RATE_28800``, ``RFM12_DATA_RATE_38400``,
   ``RFM12_DATA_RATE_57600``, or ``RFM12_DATA_RATE_115200``.
   The names indicate nominal rates in bits per second; pass the enum
   constant rather than a numeric bit rate. ``RFM12_DATA_RATE_COUNT`` is
   a count sentinel, not a selectable rate.

   This function does not communicate with the radio. The staged data rate
   is written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :param rate: Predefined data-rate selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_get_data_rate()
---------------------

.. c:function:: RFM12_result_t rfm12_get_data_rate(const RFM12_t *dev, RFM12_data_rate_t *rate)

   Get the currently staged data-rate selection.

   This function returns the staged enum value without communicating with
   the radio. It does not measure or read back the hardware bit rate.

   :param dev: RFM12 radio instance.
   :param rate: Receives the staged data-rate selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_data_rate()
-----------------------

.. c:function:: RFM12_result_t rfm12_reset_data_rate(RFM12_t *dev)

   Reset the staged data-rate selection to its default value.

   This function does not communicate with the radio. The changed data rate
   is written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
