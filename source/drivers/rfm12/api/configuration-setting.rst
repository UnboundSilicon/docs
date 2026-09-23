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
