Driver API
==========

These functions manage driver instances and operations that do not map
directly to a single numbered datasheet command.

Instance acquisition, HAL configuration, result descriptions, and getters
operate on software state without communicating with the radio.
:c:func:`rfm12_apply_to_radio` and :c:func:`rfm12_software_reset` perform
immediate SPI transfers through the configured HAL callback.

Instance Management
-------------------

Acquire statically allocated radio instances for use throughout the application.

rfm12_get_instance()
~~~~~~~~~~~~~~~~~~~~~~~~

.. c:function:: RFM12_result_t rfm12_get_instance(RFM12_t **instance)

   Acquire the next available statically allocated radio instance and load
   its staged defaults. No SPI transaction is performed.

   The instance remains valid for the lifetime of the program and must not
   be freed. Instances cannot be released or reused. This function is
   intended for application initialization and is not thread-safe.

   :param instance: Receives the opaque radio handle; set to ``NULL`` when
                    acquisition fails.
   :return: ``RFM12_OK`` on success,
            ``RFM12_ERROR_NO_INSTANCE_AVAILABLE`` when the instance pool is
            exhausted, or an appropriate :c:type:`RFM12_result_t` error.


Hardware Abstraction
--------------------

Connect a radio instance to the platform SPI implementation through its HAL
callback and context.

rfm12_configure_hal()
~~~~~~~~~~~~~~~~~~~~~~~~~

.. c:function:: RFM12_result_t rfm12_configure_hal(RFM12_t *dev, RFM12_spi_transfer16_fn function, void *context)

   Associate a radio instance with its synchronous 16-bit SPI callback and
   platform context. No SPI transaction is performed.

   The context is passed unchanged to every callback invocation. The
   callback transmits the supplied word, stores the simultaneously received
   word through its output pointer, and returns an ``RFM12_result_t``.

   :param dev: RFM12 radio instance.
   :param function: SPI transfer callback; must not be ``NULL``.
   :param context: Opaque platform context passed to the callback; may be ``NULL``.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


Configuration
-------------

Validate staged settings and apply pending configuration to the radio.

rfm12_apply_to_radio()
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. c:function:: RFM12_result_t rfm12_apply_to_radio(RFM12_t *dev)

   Validate dependent staged settings and transmit all pending configuration
   command groups to the radio.

   Groups marked dirty contain pending settings. Clean groups are skipped,
   and the Power Management Command is sent last. Each command group is
   marked clean after its transfer succeeds.

   If a transfer fails, the failed and remaining groups stay dirty for a
   later retry. Groups already transferred successfully remain clean.

   :param dev: RFM12 radio instance containing staged configuration and
               pending-command flags, which are updated as transfers succeed.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` validation or transfer error.


Device Control
--------------

Perform immediate device operations, such as resetting the physical radio.

rfm12_software_reset()
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. c:function:: RFM12_result_t rfm12_software_reset(RFM12_t *dev)

   Immediately enable sensitive reset and send the special ``0xFE00``
   software-reset command to the radio.

   The HAL configuration and staged settings are preserved. Pending
   configuration is not applied before the reset. After a successful reset
   sequence, all configuration groups are marked dirty so they can be
   restored with :c:func:`rfm12_apply_to_radio`.

   .. note::

      This function does not provide the required hardware startup delay.
      Wait for the radio to complete its reset/startup delay before applying
      the staged configuration again.

   :param dev: RFM12 radio instance whose physical radio will be reset.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


Driver State
------------

Inspect the tracked operating mode and synchronization settings stored by
the driver without reading the physical radio.

rfm12_get_mode()
~~~~~~~~~~~~~~~~~~~~

.. c:function:: RFM12_result_t rfm12_get_mode(const RFM12_t *dev, RFM12_mode_t *mode)

   Get the driver's tracked operating mode.

   This is software state; the function does not read the physical radio.
   The tracked value may be ``RFM12_MODE_UNKNOWN``, particularly after
   instance acquisition, software reset, or manual changes to
   mode-defining power bits.

   :param dev: RFM12 radio instance.
   :param mode: Receives the tracked operating mode.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


rfm12_get_sync_bytes()
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. c:function:: RFM12_result_t rfm12_get_sync_bytes(const RFM12_t *dev, uint8_t *buffer, uint8_t buffer_size, uint8_t *length)

   Build the synchronization sequence represented by the staged FIFO and
   Sync Pattern settings. No SPI transaction is performed.

   One-byte mode returns the programmable synchronization byte. Two-byte
   mode returns the fixed byte ``0x2D`` followed by the programmable byte.
   The buffer must hold at least one byte or two bytes, respectively.

   :param dev: RFM12 radio instance containing the staged synchronization settings.
   :param buffer: Receives the synchronization bytes.
   :param buffer_size: Available buffer size in bytes.
   :param length: Receives the number of synchronization bytes written.
   :return: ``RFM12_OK`` on success, or an appropriate
            :c:type:`RFM12_result_t` error.


Error Handling
--------------

Translate driver result codes into readable descriptions for diagnostics.

rfm12_result_string()
~~~~~~~~~~~~~~~~~~~~~~~~~

.. c:function:: const char *rfm12_result_string(RFM12_result_t result)

   Return a static, human-readable description of a driver result code.

   No SPI transaction is performed. The returned string must not be modified
   or freed. Unknown numeric values produce an ``Unrecognized result code``
   description.

   :param result: Result code to describe.
   :return: Pointer to a static string describing the result code.
