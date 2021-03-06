..  _usage:

=====
Usage
=====

To use sushy in a project:

.. code-block:: python

  import sushy

  s = sushy.Sushy('http://127.0.0.1:8000/redfish/v1',
                  username='foo', password='bar')

  # Get the Redfish version
  print(s.redfish_version)

  # Instantiate a system object
  sys_inst = s.get_system('437XR1138R2')


  # Using system collections


  # Instantiate a SystemCollection object
  sys_col = s.get_system_collection()

  # Print the ID of the systems available in the collection
  print(sys_col.members_identities)

  # Get a list of systems objects available in the collection
  sys_col_insts = sys_col.get_members()

  # Instantiate a system object, same as getting it directly
  # from the s.get_system()
  sys_inst = sys_col.get_member(sys_col.members_identities[0])

  # Refresh the system collection object
  sys_col.refresh()


  # Using system actions


  # Power the system ON
  sys_inst.reset_system(sushy.RESET_ON)

  # Get a list of allowed reset values
  print(sys_inst.get_allowed_reset_system_values())

  # Refresh the system object
  sys_inst.refresh()

  # Get the current power state
  print(sys_inst.power_state)

  # Set the next boot device to boot once from PXE in UEFI mode
  sys_inst.set_system_boot_source(sushy.BOOT_SOURCE_TARGET_PXE,
                                  enabled=sushy.BOOT_SOURCE_ENABLED_ONCE,
                                  mode=sushy.BOOT_SOURCE_MODE_UEFI)

  # Get the current boot source information
  print(sys_inst.boot)

  # Get a list of allowed boot source target values
  print(sys_inst.get_allowed_system_boot_source_values())

.. TODO: Get current boot source device, enabled and mode
.. TODO: Document how to setup the Redfish mockup server
