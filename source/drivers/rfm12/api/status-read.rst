17. Status Read Command
========================

Reads the radio's status word, including interrupt indications, receiver
state, and AFC information.

Register Fields
---------------

The command transmits ``0x0000`` in an immediate SPI transfer. The table
below describes the returned status word, not fields to be staged or written.

.. list-table::
   :header-rows: 1

   * - Bits
     - Name
     - Meaning
     - API
   * - 15
     - ``FFIT``
     - RX: RX FIFO has reached the configured interrupt level
     - :c:func:`rfm12_status_rx_fifo_interrupt`
   * - 15
     - ``RGIT``
     - TX: TX register is ready for the next byte
     - :c:func:`rfm12_status_tx_register_ready`
   * - 14
     - ``POR``
     - Power-on or software reset indicated
     - :c:func:`rfm12_status_power_on_reset`
   * - 13
     - ``FFOV``
     - RX: RX FIFO overflow indicated
     - :c:func:`rfm12_status_rx_fifo_overflow`
   * - 13
     - ``RGUR``
     - TX: TX register underrun indicated
     - :c:func:`rfm12_status_tx_register_underrun`
   * - 12
     - ``WKUP``
     - Wake-up timer expired
     - :c:func:`rfm12_status_wakeup_timer_expired`
   * - 11
     - ``EXT``
     - External interrupt input is active
     - :c:func:`rfm12_status_external_interrupt`
   * - 10
     - ``LBD``
     - Supply voltage is below the configured threshold
     - :c:func:`rfm12_status_low_battery`
   * - 9
     - ``FFEM``
     - RX FIFO is empty
     - :c:func:`rfm12_status_rx_fifo_empty`
   * - 8
     - ``ATS``
     - Antenna tuning circuit detected sufficient RF signal
     - :c:func:`rfm12_status_antenna_tuning_signal`
   * - 7
     - ``RSSI``
     - Received signal exceeds the configured RSSI threshold
     - :c:func:`rfm12_status_rssi_detected`
   * - 6
     - ``DQD``
     - Data Quality Detector output is high
     - :c:func:`rfm12_status_data_quality_detected`
   * - 5
     - ``CRL``
     - Clock recovery is locked
     - :c:func:`rfm12_status_clock_recovery_locked`
   * - 4
     - ``ATGL``
     - AFC cycle toggle state
     - :c:func:`rfm12_status_afc_cycle_toggle`
   * - 3:0
     - AFC offset
     - Signed four-bit offset decoded by the API
     - :c:func:`rfm12_status_afc_offset_steps`

.. note::

   Bits 15 and 13 are mode-dependent. In RX mode they report FIFO interrupt
   (``FFIT``) and overflow (``FFOV``); in TX mode they report register ready
   (``RGIT``) and underrun (``RGUR``). Use the helpers appropriate to the
   radio mode when the status word was read. RX indications require receiver
   FIFO mode and the receiver to be enabled; TX indications require the TX
   data register and transmitter to be enabled.

The :ref:`status-read-helper-functions` decode a previously read status word.
Only the command function communicates with the radio.

Data Types
----------

RFM12_status_word_t
~~~~~~~~~~~~~~~~~~~

.. c:type:: uint16_t RFM12_status_word_t

   Raw 16-bit radio status returned by :c:func:`rfm12_read_status` and consumed by the
   status helpers on this page. Bits 15 and 13 depend on RX/TX mode. Bits 3:0 contain a
   signed four-bit AFC offset; :c:func:`rfm12_status_afc_offset_steps` sign-extends it
   to int8_t. This is a status snapshot, not staged driver state.

Command Functions
-----------------

rfm12_read_status()
-----------------------

.. c:function:: RFM12_result_t rfm12_read_status(RFM12_t *dev, RFM12_status_word_t *status)

   Read the radio's status word immediately through the configured SPI callback.

   This operation does not require :c:func:`rfm12_apply_to_radio`. A status
   read can clear latched indications such as power-on reset, wake-up timer
   expiry, and FIFO overflow. It does not clear every interrupt condition:
   FIFO threshold and TX-ready indications require servicing the associated
   data path or disabling it. The datasheet's interrupt-handling section
   specifies that TX underrun remains active until the transmitter and TX
   latch are switched off.

   :param dev: RFM12 radio instance.
   :param status: Receives the 16-bit status word.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.

.. _status-read-helper-functions:

Helper Functions
----------------

These helpers decode the supplied status word without communicating with the
radio, clearing hardware flags, or updating the snapshot. The Boolean
helpers return the state of one bit. They do not check the operating mode:
helpers for the same shared bit return the same Boolean result, so the
caller must choose the appropriate RX or TX interpretation.

rfm12_status_rx_fifo_interrupt()
------------------------------------

.. c:function:: bool rfm12_status_rx_fifo_interrupt(RFM12_status_word_t status)

   Test bit 15 (``FFIT``): rX FIFO has reached the configured interrupt level.

   Interpret this result in RX mode. In TX mode, the same bit means
   ``RGIT`` instead.

   :param status: Previously read status word.
   :return: ``true`` if bit 15 is set; otherwise ``false``.


rfm12_status_tx_register_ready()
------------------------------------

.. c:function:: bool rfm12_status_tx_register_ready(RFM12_status_word_t status)

   Test bit 15 (``RGIT``): tX register is ready for the next byte.

   Interpret this result in TX mode. In RX mode, the same bit means
   ``FFIT`` instead.

   :param status: Previously read status word.
   :return: ``true`` if bit 15 is set; otherwise ``false``.


rfm12_status_power_on_reset()
---------------------------------

.. c:function:: bool rfm12_status_power_on_reset(RFM12_status_word_t status)

   Test bit 14 (``POR``): power-on or software reset indicated.

   :param status: Previously read status word.
   :return: ``true`` if bit 14 is set; otherwise ``false``.


rfm12_status_rx_fifo_overflow()
-----------------------------------

.. c:function:: bool rfm12_status_rx_fifo_overflow(RFM12_status_word_t status)

   Test bit 13 (``FFOV``): rX FIFO overflow indicated.

   Interpret this result in RX mode. In TX mode, the same bit means
   ``RGUR`` instead.

   :param status: Previously read status word.
   :return: ``true`` if bit 13 is set; otherwise ``false``.


rfm12_status_tx_register_underrun()
---------------------------------------

.. c:function:: bool rfm12_status_tx_register_underrun(RFM12_status_word_t status)

   Test bit 13 (``RGUR``): tX register underrun indicated.

   Interpret this result in TX mode. In RX mode, the same bit means
   ``FFOV`` instead.

   :param status: Previously read status word.
   :return: ``true`` if bit 13 is set; otherwise ``false``.


rfm12_status_wakeup_timer_expired()
---------------------------------------

.. c:function:: bool rfm12_status_wakeup_timer_expired(RFM12_status_word_t status)

   Test bit 12 (``WKUP``): wake-up timer expired.

   :param status: Previously read status word.
   :return: ``true`` if bit 12 is set; otherwise ``false``.


rfm12_status_external_interrupt()
-------------------------------------

.. c:function:: bool rfm12_status_external_interrupt(RFM12_status_word_t status)

   Test bit 11 (``EXT``): external interrupt input is active.

   This indication follows the external interrupt input when pin 16 is
   configured for that function.

   :param status: Previously read status word.
   :return: ``true`` if bit 11 is set; otherwise ``false``.


rfm12_status_low_battery()
------------------------------

.. c:function:: bool rfm12_status_low_battery(RFM12_status_word_t status)

   Test bit 10 (``LBD``): supply voltage is below the configured threshold.

   The low-battery detector must be enabled. The status bit remains active
   while the supply is below the threshold, even after a status read.

   :param status: Previously read status word.
   :return: ``true`` if bit 10 is set; otherwise ``false``.


rfm12_status_rx_fifo_empty()
--------------------------------

.. c:function:: bool rfm12_status_rx_fifo_empty(RFM12_status_word_t status)

   Test bit 9 (``FFEM``): rX FIFO is empty.

   :param status: Previously read status word.
   :return: ``true`` if bit 9 is set; otherwise ``false``.


rfm12_status_antenna_tuning_signal()
----------------------------------------

.. c:function:: bool rfm12_status_antenna_tuning_signal(RFM12_status_word_t status)

   Test bit 8 (``ATS``): antenna tuning circuit detected sufficient RF signal.

   :param status: Previously read status word.
   :return: ``true`` if bit 8 is set; otherwise ``false``.


rfm12_status_rssi_detected()
--------------------------------

.. c:function:: bool rfm12_status_rssi_detected(RFM12_status_word_t status)

   Test bit 7 (``RSSI``): received signal exceeds the configured RSSI threshold.

   :param status: Previously read status word.
   :return: ``true`` if bit 7 is set; otherwise ``false``.


rfm12_status_data_quality_detected()
----------------------------------------

.. c:function:: bool rfm12_status_data_quality_detected(RFM12_status_word_t status)

   Test bit 6 (``DQD``): data Quality Detector output is high.

   :param status: Previously read status word.
   :return: ``true`` if bit 6 is set; otherwise ``false``.


rfm12_status_clock_recovery_locked()
----------------------------------------

.. c:function:: bool rfm12_status_clock_recovery_locked(RFM12_status_word_t status)

   Test bit 5 (``CRL``): clock recovery is locked.

   :param status: Previously read status word.
   :return: ``true`` if bit 5 is set; otherwise ``false``.


rfm12_status_afc_cycle_toggle()
-----------------------------------

.. c:function:: bool rfm12_status_afc_cycle_toggle(RFM12_status_word_t status)

   Test bit 4 (``ATGL``): aFC cycle toggle state.

   This bit toggles on each AFC cycle. Compare successive snapshots to
   detect a change; a high bit alone is not a new-cycle event.

   :param status: Previously read status word.
   :return: ``true`` if bit 4 is set; otherwise ``false``.


rfm12_status_afc_offset_steps()
----------------------------------

.. c:function:: int8_t rfm12_status_afc_offset_steps(RFM12_status_word_t status)

   Decode bits 3:0 as a signed four-bit AFC offset and sign-extend it to
   ``int8_t``, as specified by the header's API contract.

   The result ranges from -8 through +7 steps. One PLL frequency step is
   2.5 kHz in the 433 MHz band, 5 kHz in the 868 MHz band, or 7.5 kHz in
   the 915 MHz band.

   .. note::

      The datasheet also describes a separate ``OFFS(6)`` sign indication
      in the status-read sequence. This helper's documented contract
      decodes only bits 3:0; it does not reconstruct a wider offset value.

   For accurate offset readings, the datasheet requires AFC calculation
   to be disabled during the read. Stage the disabled setting with
   :c:func:`rfm12_set_afc_enable` and apply it before calling
   :c:func:`rfm12_read_status`.

   :param status: Previously read status word.
   :return: Signed four-bit AFC offset in frequency steps.
