import storage
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "DACTYLL"  # or DACTYLR for left side
storage.enable_usb_drive()
