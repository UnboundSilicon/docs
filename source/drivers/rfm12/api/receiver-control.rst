5. Receiver Control Command
===========================

Configures receiver bandwidth, low-noise amplifier (LNA) gain, received signal
strength indicator (RSSI) threshold, valid data indicator (VDI) behavior, and
the function of pin 16.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 10
     - ``p16``
     - Pin 16 function
     - :c:func:`rfm12_set_pin16_function`
   * - 9:8
     - ``d1:d0``
     - VDI response mode
     - :c:func:`rfm12_set_vdi_mode`
   * - 7:5
     - ``i2:i0``
     - Receiver baseband bandwidth
     - :c:func:`rfm12_set_rx_bandwidth`
   * - 4:3
     - ``g1:g0``
     - LNA gain
     - :c:func:`rfm12_set_lna_gain`
   * - 2:0
     - ``r2:r0``
     - RSSI detector threshold
     - :c:func:`rfm12_set_rssi_threshold`

The functions listed in the register field table above directly configure
fields in the Receiver Control Command. The setters and reset function
update staged configuration without communicating with the radio. Use
:c:func:`rfm12_apply_to_radio` to write the staged settings.

Data Types
----------

RFM12_pin16_function_t
~~~~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_pin16_function_t

   Enum. Pin 16 function selection for bit 10.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_PIN16_INTERRUPT_IN``
        - ``0``
        - External interrupt input.
      * - ``RFM12_PIN16_VDI_OUT``
        - ``1``
        - VDI output.


RFM12_vdi_mode_t
~~~~~~~~~~~~~~~~

.. c:type:: RFM12_vdi_mode_t

   Enum. Valid Data Indicator (VDI) response selection for bits 9:8.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_VDI_FAST``
        - ``0``
        - Fast response.
      * - ``RFM12_VDI_MEDIUM``
        - ``1``
        - Medium response.
      * - ``RFM12_VDI_SLOW``
        - ``2``
        - Slow response.
      * - ``RFM12_VDI_ALWAYS``
        - ``3``
        - VDI always on.


RFM12_rx_bandwidth_t
~~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_rx_bandwidth_t

   Enum. Receiver baseband bandwidth selection for bits 7:5. Encodings 0 and 7 are not
   supported.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_RX_BANDWIDTH_400_KHZ``
        - ``1``
        - 400 kHz.
      * - ``RFM12_RX_BANDWIDTH_340_KHZ``
        - ``2``
        - 340 kHz.
      * - ``RFM12_RX_BANDWIDTH_270_KHZ``
        - ``3``
        - 270 kHz.
      * - ``RFM12_RX_BANDWIDTH_200_KHZ``
        - ``4``
        - 200 kHz.
      * - ``RFM12_RX_BANDWIDTH_134_KHZ``
        - ``5``
        - 134 kHz.
      * - ``RFM12_RX_BANDWIDTH_67_KHZ``
        - ``6``
        - 67 kHz.


RFM12_lna_gain_t
~~~~~~~~~~~~~~~~

.. c:type:: RFM12_lna_gain_t

   Enum. Low-noise amplifier gain relative to maximum gain, encoded in bits 4:3.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_LNA_GAIN_0_DB``
        - ``0``
        - 0 dB.
      * - ``RFM12_LNA_GAIN_M6_DB``
        - ``1``
        - -6 dB.
      * - ``RFM12_LNA_GAIN_M14_DB``
        - ``2``
        - -14 dB.
      * - ``RFM12_LNA_GAIN_M20_DB``
        - ``3``
        - -20 dB.


RFM12_rssi_threshold_t
~~~~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_rssi_threshold_t

   Enum. RSSI detector threshold selection for bits 2:0. The effective threshold is the
   selected threshold plus the LNA gain in dB. Encodings 6 and 7 are not supported.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_RSSI_THRESHOLD_M103_DBM``
        - ``0``
        - -103 dBm.
      * - ``RFM12_RSSI_THRESHOLD_M97_DBM``
        - ``1``
        - -97 dBm.
      * - ``RFM12_RSSI_THRESHOLD_M91_DBM``
        - ``2``
        - -91 dBm.
      * - ``RFM12_RSSI_THRESHOLD_M85_DBM``
        - ``3``
        - -85 dBm.
      * - ``RFM12_RSSI_THRESHOLD_M79_DBM``
        - ``4``
        - -79 dBm.
      * - ``RFM12_RSSI_THRESHOLD_M73_DBM``
        - ``5``
        - -73 dBm.

Command Functions
-----------------

rfm12_set_pin16_function()
--------------------------

.. c:function:: RFM12_result_t rfm12_set_pin16_function(RFM12_t *dev, RFM12_pin16_function_t pin16)

   Stage the function of pin 16.

   Select ``RFM12_PIN16_INTERRUPT_IN`` for the external interrupt input or
   ``RFM12_PIN16_VDI_OUT`` for the valid data indicator output.

   :param dev: RFM12 radio instance.
   :param pin16: Pin 16 function to select.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_vdi_mode()
--------------------

.. c:function:: RFM12_result_t rfm12_set_vdi_mode(RFM12_t *dev, RFM12_vdi_mode_t mode)

   Stage the valid data indicator response mode.

   Select ``RFM12_VDI_FAST``, ``RFM12_VDI_MEDIUM``, ``RFM12_VDI_SLOW``,
   or ``RFM12_VDI_ALWAYS``. The always-on mode holds VDI high independently
   of the receiving parameters.

   :param dev: RFM12 radio instance.
   :param mode: VDI response mode to select.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_rx_bandwidth()
------------------------

.. c:function:: RFM12_result_t rfm12_set_rx_bandwidth(RFM12_t *dev, RFM12_rx_bandwidth_t bandwidth)

   Stage the receiver baseband bandwidth.

   Select ``RFM12_RX_BANDWIDTH_400_KHZ``, ``RFM12_RX_BANDWIDTH_340_KHZ``,
   ``RFM12_RX_BANDWIDTH_270_KHZ``, ``RFM12_RX_BANDWIDTH_200_KHZ``,
   ``RFM12_RX_BANDWIDTH_134_KHZ``, or ``RFM12_RX_BANDWIDTH_67_KHZ``.

   :param dev: RFM12 radio instance.
   :param bandwidth: Receiver bandwidth selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_lna_gain()
--------------------

.. c:function:: RFM12_result_t rfm12_set_lna_gain(RFM12_t *dev, RFM12_lna_gain_t gain)

   Stage the low-noise amplifier gain relative to its maximum gain.

   Select ``RFM12_LNA_GAIN_0_DB``, ``RFM12_LNA_GAIN_M6_DB``,
   ``RFM12_LNA_GAIN_M14_DB``, or ``RFM12_LNA_GAIN_M20_DB`` for 0, -6,
   -14, or -20 dB respectively. The LNA gain also affects the effective
   RSSI threshold configured by :c:func:`rfm12_set_rssi_threshold`.

   :param dev: RFM12 radio instance.
   :param gain: LNA gain selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_rssi_threshold()
--------------------------

.. c:function:: RFM12_result_t rfm12_set_rssi_threshold(RFM12_t *dev, RFM12_rssi_threshold_t threshold)

   Stage the RSSI detector threshold setting.

   Select ``RFM12_RSSI_THRESHOLD_M103_DBM``,
   ``RFM12_RSSI_THRESHOLD_M97_DBM``, ``RFM12_RSSI_THRESHOLD_M91_DBM``,
   ``RFM12_RSSI_THRESHOLD_M85_DBM``, ``RFM12_RSSI_THRESHOLD_M79_DBM``,
   or ``RFM12_RSSI_THRESHOLD_M73_DBM``.

   The effective RSSI threshold depends on the LNA gain. The datasheet
   expresses this relationship as ``RSSI_th = RSSI_setth + G_LNA``.

   :param dev: RFM12 radio instance.
   :param threshold: RSSI detector threshold selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_receiver_control()
------------------------------

.. c:function:: RFM12_result_t rfm12_reset_receiver_control(RFM12_t *dev)

   Reset the staged Receiver Control Command values to their defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
