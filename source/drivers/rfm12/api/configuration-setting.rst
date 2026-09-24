1. Configuration Setting Command
================================

Configures the data-register paths, frequency band, and crystal load
capacitance.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7
     - ``el``
     - TX data register enable
     - :c:func:`rfm12_set_tx_data_register_enable`
   * - 6
     - ``ef``
     - RX FIFO enable
     - :c:func:`rfm12_set_rx_fifo_enable`
   * - 5:4
     - ``b1:b0``
     - Frequency band
     - :c:func:`rfm12_set_frequency_band`
   * - 3:0
     - ``x3:x0``
     - Crystal load capacitance
     - :c:func:`rfm12_set_xtal_cap`

Data Types
----------

RFM12_frequency_band_t
~~~~~~~~~~~~~~~~~~~~~~

.. c:type:: RFM12_frequency_band_t

   Enum. Frequency-band selection for bits 5:4. Select the band before setting the
   carrier frequency with :c:func:`rfm12_set_frequency`.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_BAND_433``
        - ``1``
        - 433 MHz band.
      * - ``RFM12_BAND_868``
        - ``2``
        - 868 MHz band.
      * - ``RFM12_BAND_915``
        - ``3``
        - 915 MHz band.


RFM12_xtal_cap_t
~~~~~~~~~~~~~~~~

.. c:type:: RFM12_xtal_cap_t

   Enum. Crystal load capacitance for bits 3:0, in 0.5 pF steps from 8.5 through 16.0
   pF.

   .. list-table::
      :header-rows: 1

      * - Constant
        - Value
        - Meaning
      * - ``RFM12_XTAL_CAP_8_5PF``
        - ``0``
        - 8.5 pF.
      * - ``RFM12_XTAL_CAP_9_0PF``
        - ``1``
        - 9.0 pF.
      * - ``RFM12_XTAL_CAP_9_5PF``
        - ``2``
        - 9.5 pF.
      * - ``RFM12_XTAL_CAP_10_0PF``
        - ``3``
        - 10.0 pF.
      * - ``RFM12_XTAL_CAP_10_5PF``
        - ``4``
        - 10.5 pF.
      * - ``RFM12_XTAL_CAP_11_0PF``
        - ``5``
        - 11.0 pF.
      * - ``RFM12_XTAL_CAP_11_5PF``
        - ``6``
        - 11.5 pF.
      * - ``RFM12_XTAL_CAP_12_0PF``
        - ``7``
        - 12.0 pF.
      * - ``RFM12_XTAL_CAP_12_5PF``
        - ``8``
        - 12.5 pF.
      * - ``RFM12_XTAL_CAP_13_0PF``
        - ``9``
        - 13.0 pF.
      * - ``RFM12_XTAL_CAP_13_5PF``
        - ``10``
        - 13.5 pF.
      * - ``RFM12_XTAL_CAP_14_0PF``
        - ``11``
        - 14.0 pF.
      * - ``RFM12_XTAL_CAP_14_5PF``
        - ``12``
        - 14.5 pF.
      * - ``RFM12_XTAL_CAP_15_0PF``
        - ``13``
        - 15.0 pF.
      * - ``RFM12_XTAL_CAP_15_5PF``
        - ``14``
        - 15.5 pF.
      * - ``RFM12_XTAL_CAP_16_0PF``
        - ``15``
        - 16.0 pF.

Command Functions
-----------------

rfm12_set_tx_data_register_enable()
-----------------------------------

.. c:function:: RFM12_result_t rfm12_set_tx_data_register_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the TX data register enable setting.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the TX data register.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_rx_fifo_enable()
--------------------------

.. c:function:: RFM12_result_t rfm12_set_rx_fifo_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the RX FIFO enable setting.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the RX FIFO.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_frequency_band()
--------------------------

.. c:function:: RFM12_result_t rfm12_set_frequency_band(RFM12_t *dev, RFM12_frequency_band_t band)

   Stage the operating frequency band.

   :param dev: RFM12 radio instance.
   :param band: Frequency band to select.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_xtal_cap()
--------------------

.. c:function:: RFM12_result_t rfm12_set_xtal_cap(RFM12_t *dev, RFM12_xtal_cap_t cap)

   Stage the crystal load capacitance setting.

   :param dev: RFM12 radio instance.
   :param cap: Crystal load capacitance setting.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_config_setting()
----------------------------

.. c:function:: RFM12_result_t rfm12_reset_config_setting(RFM12_t *dev)

   Reset the staged Configuration Setting Command values to their defaults.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
