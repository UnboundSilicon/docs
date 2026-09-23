12. PLL Setting Command
========================

Configures the microcontroller clock output-buffer drive, phase-detector
delay, PLL dithering, and PLL bandwidth.

.. note::

   The datasheet recommends retaining the power-on-reset settings for typical
   applications. Changes should be checked by examining the output RF spectrum.

Register Fields
---------------

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 7
     - Fixed
     - Must be ``0``
     - None
   * - 6:5
     - ``ob1:ob0``
     - CLK output-buffer drive current
     - :c:func:`rfm12_set_pll_output_buffer_current`
   * - 4
     - Fixed
     - Must be ``1``
     - None
   * - 3
     - ``dly``
     - Phase-detector delay enable
     - :c:func:`rfm12_set_pll_delay_enable`
   * - 2
     - ``ddit``
     - PLL dithering disable
     - :c:func:`rfm12_set_pll_dithering_disable`
   * - 1
     - Fixed
     - Must be ``1``
     - None
   * - 0
     - ``bw0``
     - PLL bandwidth
     - :c:func:`rfm12_set_pll_bandwidth`

The setters listed in the register field table above directly configure
fields in the PLL Setting Command. The setters and reset function update
staged configuration without communicating with the radio. Use
:c:func:`rfm12_apply_to_radio` to write the staged settings.

Command Functions
-----------------

rfm12_set_pll_output_buffer_current()
----------------------------------------

.. c:function:: RFM12_result_t rfm12_set_pll_output_buffer_current(RFM12_t *dev, RFM12_pll_output_buffer_current_t current)

   Stage the drive-current selection for the microcontroller CLK output.

   Higher drive current produces faster rise and fall times but can cause
   interference. The datasheet relates the selections to the CLK frequency
   as follows; the optimal setting also depends on external load capacitance.

   .. list-table::
      :header-rows: 1

      * - Selection
        - ``ob1:ob0``
        - CLK frequency
      * - ``RFM12_PLL_OUTPUT_BUFFER_CURRENT_0``
        - ``00``
        - 2.5 MHz or less
      * - ``RFM12_PLL_OUTPUT_BUFFER_CURRENT_1``
        - ``01``
        - 2.5 MHz or less
      * - ``RFM12_PLL_OUTPUT_BUFFER_CURRENT_2``
        - ``10``
        - 3.3 MHz
      * - ``RFM12_PLL_OUTPUT_BUFFER_CURRENT_3``
        - ``11``
        - 5 or 10 MHz (recommended)

   This setting controls output drive, not the clock division ratio.

   :param dev: RFM12 radio instance.
   :param current: CLK output-buffer drive-current selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_pll_delay_enable()
--------------------------------

.. c:function:: RFM12_result_t rfm12_set_pll_delay_enable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the PLL phase-detector delay setting.

   Enabling this setting sets ``dly`` and switches on the delay in the
   phase detector.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the phase-detector delay.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_pll_dithering_disable()
------------------------------------

.. c:function:: RFM12_result_t rfm12_set_pll_dithering_disable(RFM12_t *dev, RFM12_enable_t enable)

   Stage the PLL dithering-disable setting.

   Enabling this setting sets ``ddit`` and disables dithering in the PLL
   loop. Disabling this setting clears ``ddit`` and allows dithering.

   :param dev: RFM12 radio instance.
   :param enable: Enable or disable the dithering-disable bit.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_set_pll_bandwidth()
----------------------------

.. c:function:: RFM12_result_t rfm12_set_pll_bandwidth(RFM12_t *dev, RFM12_pll_bandwidth_t bandwidth)

   Stage the PLL loop bandwidth for transmitter RF performance.

   Select ``RFM12_PLL_BANDWIDTH_NORMAL`` for ``bw0 = 0`` or
   ``RFM12_PLL_BANDWIDTH_HIGH`` for ``bw0 = 1``. The datasheet lists the
   following tradeoff between maximum bit rate and phase noise.

   .. list-table::
      :header-rows: 1

      * - Selection
        - Maximum bit rate
        - Phase noise at 1 MHz offset
      * - ``RFM12_PLL_BANDWIDTH_NORMAL``
        - 86.2 kbps
        - -107 dBc/Hz
      * - ``RFM12_PLL_BANDWIDTH_HIGH``
        - 256 kbps
        - -102 dBc/Hz

   These are hardware PLL characteristics; this setter does not select
   the data rate. The datasheet power-on-reset command value is ``0xCC77``,
   which has ``bw0 = 1``. The header's comment labeling the normal
   bandwidth selection as the default does not describe that hardware
   power-on-reset value.

   :param dev: RFM12 radio instance.
   :param bandwidth: PLL loop-bandwidth selection.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_reset_pll_setting()
----------------------------

.. c:function:: RFM12_result_t rfm12_reset_pll_setting(RFM12_t *dev)

   Reset the staged PLL Setting Command values to their library defaults.

   This function does not communicate with the radio. The changed settings
   are written to the radio by :c:func:`rfm12_apply_to_radio`.

   :param dev: RFM12 radio instance.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.
