import os

res_layout = "f:/srushti/AdminApp/app/src/main/res/layout"
java_dir = "f:/srushti/AdminApp/app/src/main/java/com/example/adminapp"

activities = ["CategoryActivity", "ProductActivity", "UserActivity", "UserDetailsActivity", "OrderActivity", "OrderDetailsActivity"]
for act in activities:
    layout_name = "activity_" + act.replace("Activity", "").lower()
    
    # Create empty layout
    with open(os.path.join(res_layout, f"{layout_name}.xml"), "w") as f:
        f.write(f"""<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <!-- To be implemented -->
</androidx.constraintlayout.widget.ConstraintLayout>
""")

    # Create empty activity
    with open(os.path.join(java_dir, f"{act}.kt"), "w") as f:
        f.write(f"""package com.example.adminapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class {act} : AppCompatActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        setContentView(R.layout.{layout_name})
    }}
}}
""")

print("Stub activities and layouts generated.")
