10. AFC Command
================

Configures automatic frequency control (AFC), which measures the transmitter
and receiver frequency offset and can adjust the receiver frequency to
compensate for it.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7:6
     - ``a1:a0``
     - AFC operating mode
     - :c:func:`rfm12_set_afc_mode`
   * - 5:4
     - ``rl1:rl0``
     - AFC range limit
     - :c:func:`rfm12_set_afc_range_limit`
   * - 3
     - ``st``
     - Store-offset strobe
     - :c:func:`rfm12_set_afc_store_offset`
   * - 2
     - ``fi``
     - Fine mode
     - :c:func:`rfm12_set_afc_fine_mode`
   * - 1
     - ``oe``
     - Offset-register output enable
     - :c:func:`rfm12_set_afc_output_register_enable`
   * - 0
     - ``en``
     - AFC calculation enable
     - :c:func:`rfm12_set_afc_enable`

The functions listed in the register field table above directly configure
fields in the AFC Command. The setters and reset function update staged
configuration without communicating with the radio. Use
:c:func:`rfm12_apply_to_radio` to write the staged settings.

Command Functions
-----------------

rfm12_set_afc_mode()
--------------------

.. c:function:: RFM12_result_t rfm12_set_afc_mode(RFM12_t *dev, RFM12_afc_mode_t mode)

   Stage the AFC automatic operating mode.

   The following table maps the header's enum names to the datasheet
   behavior of their encoded values.

   .. list-table::
      :header-rows: 1

      * - Selection
        - ``a1:a0``
        - Behavior
      * - ``RFM12_AFC_MODE_OFF``
        - ``00``
        - Automatic operation off; the microcontroller controls the strobe.
      * - ``RFM12_AFC_MODE_ON``
        - ``01``
        - Runs once after each power-up.
      * - ``RFM12_AFC_MODE_ON_AFTER_RECEIVING``
        - ``10``
        - Retains the offset only during reception while VDI is high.
      * - ``RFM12_AFC_MODE_KEEP_OFFSET_ON_RECEIVE``
        - ``11``
        - Retains the offset independently of the VDI signal.

   :param dev: RFM12 radio instance.
   :param mode: AFC operating mode selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_afc_range_limit()
---------------------------

.. c:function:: RFM12_result_t rfm12_set_afc_range_limit(RFM12_t *dev, RFM12_afc_range_t range_limit)

   Stage the allowed range of the AFC frequency-offset register.

   .. list-table::
      :header-rows: 1

      * - Selection
        - Offset range in frequency steps
      * - ``RFM12_AFC_RANGE_UNRESTRICTED``
        - No range restriction
      * - ``RFM12_AFC_RANGE_15_TO_16``
        - -16 through +15
      * - ``RFM12_AFC_RANGE_7_TO_8``
        - -8 through +7
      * - ``RFM12_AFC_RANGE_3_TO_4``
        - -4 through +3

   One frequency step is 2.5 kHz in the 433 MHz band, 5 kHz in the
   868 MHz band, or 7.5 kHz in the 915 MHz band.

   :param dev: RFM12 radio instance.
   :param range_limit: AFC frequency-offset range selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_afc_store_offset()
----------------------------

.. c:function:: RFM12_result_t rfm12_set_afc_store_offset(RFM12_t *dev, RFM12_enable_t enable)

   Stage the store-offset strobe bit.

   A rising edge on the hardware ``st`` bit stores the latest calculated
   frequency error in the AFC offset register. This setter stages the bit
   level; it does not immediately generate a strobe.

   To generate another rising edge when ``st`` is already high, stage and
   apply the disabled setting, then stage and apply the enabled setting.
   Staging both levels before a single apply does not transmit both edges.

   :param dev: RFM12 radio instance.
   :param enable: Set or clear the store-offset strobe bit.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_afc_fine_mode()
-------------------------

.. c:function:: RFM12_result_t rfm12_set_afc_fine_mode(RFM12_t *dev, RFM12_enable_t enable)

   Stage the AFC fine-mode setting.

   Fine mode approximately doubles the processing time and halves the
   measurement uncertainty compared with normal operation.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable high-accuracy AFC fine mode.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_afc_output_register_enable()
--------------------------------------

.. c:function:: RFM12_result_t rfm12_set_afc_output_register_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the AFC offset-register output enable setting.

   Enabling this setting allows the stored offset to be added to the PLL
   frequency control word. Offset calculation is controlled separately by
   :c:func:`rfm12_set_afc_enable`.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable application of the stored frequency offset.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_afc_enable()
----------------------

.. c:function:: RFM12_result_t rfm12_set_afc_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the AFC frequency-offset calculation enable setting.

   Applying the calculated offset to the PLL is controlled separately by
   :c:func:`rfm12_set_afc_output_register_enable`.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable frequency-offset calculation by the AFC circuit.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_afc()
-----------------

.. c:function:: RFM12_result_t rfm12_reset_afc(RFM12_t *dev)

   Reset the staged AFC Command values to their defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
