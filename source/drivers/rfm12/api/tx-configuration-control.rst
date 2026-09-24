11. TX Configuration Control Command
=====================================

Configures FSK modulation polarity, frequency deviation, and transmitter
output power.

Register Fields
-------------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 8
     - ``mp``
     - FSK modulation polarity
     - :c:func:`rfm12_set_tx_fsk_polarity`
   * - 7:4
     - ``m3:m0``
     - FSK frequency deviation
     - :c:func:`rfm12_set_tx_fsk_deviation`
   * - 3
     - Fixed
     - Must be ``0``
     - None
   * - 2:0
     - ``p2:p0``
     - Output-power attenuation
     - :c:func:`rfm12_set_tx_power`

The setters listed in the register field table above directly configure
fields in the TX Configuration Control Command. The setters and reset
function update staged configuration without communicating with the radio.
Use :c:func:`rfm12_apply_to_radio` to write the staged settings.

Data Types
----------

RFM12_tx_fsk_polarity_t
~~~~~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_tx_fsk_polarity_t

   Enum. FSK data polarity selection for bit 8.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_TX_FSK_POLARITY_NORMAL``
        - ``0``
        - Logic 0 selects higher frequency; logic 1 selects lower frequency.
      * - ``RFM12_TX_FSK_POLARITY_INVERTED``
        - ``1``
        - Logic 0 selects lower frequency; logic 1 selects higher frequency.


RFM12_tx_fsk_deviation_t
~~~~~~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_tx_fsk_deviation_t

   Enum. FSK frequency deviation for bits 7:4, in 15 kHz steps from 15 through 240 kHz.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_TX_FSK_DEVIATION_15KHZ``
        - ``0``
        - 15 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_30KHZ``
        - ``1``
        - 30 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_45KHZ``
        - ``2``
        - 45 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_60KHZ``
        - ``3``
        - 60 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_75KHZ``
        - ``4``
        - 75 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_90KHZ``
        - ``5``
        - 90 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_105KHZ``
        - ``6``
        - 105 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_120KHZ``
        - ``7``
        - 120 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_135KHZ``
        - ``8``
        - 135 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_150KHZ``
        - ``9``
        - 150 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_165KHZ``
        - ``10``
        - 165 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_180KHZ``
        - ``11``
        - 180 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_195KHZ``
        - ``12``
        - 195 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_210KHZ``
        - ``13``
        - 210 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_225KHZ``
        - ``14``
        - 225 kHz.
      * - ``RFM12_TX_FSK_DEVIATION_240KHZ``
        - ``15``
        - 240 kHz.


RFM12_tx_power_t
~~~~~~~~~~~~~~~~

.. c:type:: RFM12_tx_power_t

   Enum. Output power attenuation relative to maximum output for bits 2:0. Values
   describe relative attenuation in dB, not absolute output in dBm.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_TX_POWER_0DB``
        - ``0``
        - 0 dB.
      * - ``RFM12_TX_POWER_MINUS_2_5DB``
        - ``1``
        - -2.5 dB.
      * - ``RFM12_TX_POWER_MINUS_5DB``
        - ``2``
        - -5 dB.
      * - ``RFM12_TX_POWER_MINUS_7_5DB``
        - ``3``
        - -7.5 dB.
      * - ``RFM12_TX_POWER_MINUS_10DB``
        - ``4``
        - -10 dB.
      * - ``RFM12_TX_POWER_MINUS_12_5DB``
        - ``5``
        - -12.5 dB.
      * - ``RFM12_TX_POWER_MINUS_15DB``
        - ``6``
        - -15 dB.
      * - ``RFM12_TX_POWER_MINUS_17_5DB``
        - ``7``
        - -17.5 dB.

Command Functions
---------------------

rfm12_set_tx_fsk_polarity()
-------------------------------

.. c:function:: RFM12_result_t rfm12_set_tx_fsk_polarity(RFM12_t *dev, RFM12_tx_fsk_polarity_t polarity)

   Stage the FSK modulation polarity.

   Select ``RFM12_TX_FSK_POLARITY_NORMAL`` for ``mp = 0``: logic 0
   produces the higher frequency and logic 1 produces the lower frequency.
   Select ``RFM12_TX_FSK_POLARITY_INVERTED`` for ``mp = 1``: logic 0
   produces the lower frequency and logic 1 produces the higher frequency.

   The datasheet defines the output frequency as
   ``f_out = f0 + (-1)^SIGN * (M + 1) * 15 kHz``, where
   ``SIGN = mp XOR FSK``, ``FSK`` is the transmitted data bit, ``M`` is
   the encoded deviation field, and ``f0`` is the carrier center frequency.

   :param dev: RFM12 radio instance.
   :param polarity: FSK modulation polarity selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_tx_fsk_deviation()
--------------------------------

.. c:function:: RFM12_result_t rfm12_set_tx_fsk_deviation(RFM12_t *dev, RFM12_tx_fsk_deviation_t deviation)

   Stage the FSK frequency deviation from the carrier center frequency.

   Select a predefined deviation from ``RFM12_TX_FSK_DEVIATION_15KHZ``
   through ``RFM12_TX_FSK_DEVIATION_240KHZ`` in 15 kHz increments.
   Pass the enum constant rather than a numeric frequency.

   The deviation magnitude is ``(M + 1) * 15 kHz``, where ``M`` is the
   four-bit ``m3:m0`` field. The two FSK frequencies lie this distance
   above and below the center frequency, so their separation is twice
   the selected deviation.

   :param dev: RFM12 radio instance.
   :param deviation: Predefined FSK frequency-deviation selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_tx_power()
------------------------

.. c:function:: RFM12_result_t rfm12_set_tx_power(RFM12_t *dev, RFM12_tx_power_t power)

   Stage the transmitter output-power selection.

   .. list-table::
      :header-rows: 1

      * - Selection
        - ``p2:p0``
        - Relative output power
      * - ``RFM12_TX_POWER_0DB``
        - ``000``
        - 0 dB (maximum output)
      * - ``RFM12_TX_POWER_MINUS_2_5DB``
        - ``001``
        - -2.5 dB
      * - ``RFM12_TX_POWER_MINUS_5DB``
        - ``010``
        - -5 dB
      * - ``RFM12_TX_POWER_MINUS_7_5DB``
        - ``011``
        - -7.5 dB
      * - ``RFM12_TX_POWER_MINUS_10DB``
        - ``100``
        - -10 dB
      * - ``RFM12_TX_POWER_MINUS_12_5DB``
        - ``101``
        - -12.5 dB
      * - ``RFM12_TX_POWER_MINUS_15DB``
        - ``110``
        - -15 dB
      * - ``RFM12_TX_POWER_MINUS_17_5DB``
        - ``111``
        - -17.5 dB

   Select attenuation from maximum output in 2.5 dB increments, from
   0 dB through 17.5 dB, using the enum constants above.

   These values are relative to maximum available output power, not
   absolute power in dBm. Maximum available power depends on antenna
   impedance.

   :param dev: RFM12 radio instance.
   :param power: Transmitter output-power selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_tx_configuration()
----------------------------------

.. c:function:: RFM12_result_t rfm12_reset_tx_configuration(RFM12_t *dev)

   Reset the staged TX Configuration Control Command values to their defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
