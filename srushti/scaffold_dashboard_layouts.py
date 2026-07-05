import os

res_layout = "f:/srushti/AdminApp/app/src/main/res/layout"
res_menu = "f:/srushti/AdminApp/app/src/main/res/menu"

activity_dashboard = """<?xml version="1.0" encoding="utf-8"?>
<androidx.drawerlayout.widget.DrawerLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/drawerLayout"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:openDrawer="start">

    <include
        android:id="@+id/appBar"
        layout="@layout/app_bar_dashboard"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

    <com.google.android.material.navigation.NavigationView
        android:id="@+id/navigationView"
        android:layout_width="wrap_content"
        android:layout_height="match_parent"
        android:layout_gravity="start"
        android:fitsSystemWindows="true"
        app:headerLayout="@layout/nav_header"
        app:menu="@menu/nav_menu" />

</androidx.drawerlayout.widget.DrawerLayout>
"""

app_bar_dashboard = """<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.google.android.material.appbar.AppBarLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:theme="@style/Theme.AdminApp.NoActionBar">

        <androidx.appcompat.widget.Toolbar
            android:id="@+id/toolbar"
            android:layout_width="match_parent"
            android:layout_height="?attr/actionBarSize"
            android:background="?attr/colorPrimary"
            app:popupTheme="@style/Theme.AdminApp"
            app:titleTextColor="@color/white"/>

    </com.google.android.material.appbar.AppBarLayout>

    <include layout="@layout/content_dashboard" />

</androidx.coordinatorlayout.widget.CoordinatorLayout>
"""

nav_header = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="176dp"
    android:background="@color/primary"
    android:gravity="bottom"
    android:orientation="vertical"
    android:padding="16dp"
    android:theme="@style/Theme.AdminApp.NoActionBar">

    <ImageView
        android:layout_width="64dp"
        android:layout_height="64dp"
        android:paddingTop="8dp"
        android:src="@mipmap/ic_launcher_round" />

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:paddingTop="8dp"
        android:text="Admin Panel"
        android:textColor="@color/white"
        android:textSize="20sp"
        android:textStyle="bold" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="admin@example.com"
        android:textColor="@color/white" />

</LinearLayout>
"""

nav_menu = """<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <group android:checkableBehavior="single">
        <item
            android:id="@+id/nav_dashboard"
            android:title="Dashboard" />
        <item
            android:id="@+id/nav_categories"
            android:title="Categories" />
        <item
            android:id="@+id/nav_products"
            android:title="Products" />
        <item
            android:id="@+id/nav_users"
            android:title="Users" />
        <item
            android:id="@+id/nav_orders"
            android:title="Orders" />
    </group>
    <item android:title="Settings">
        <menu>
            <item
                android:id="@+id/nav_logout"
                android:title="Logout" />
        </menu>
    </item>
</menu>
"""

content_dashboard = """<?xml version="1.0" encoding="utf-8"?>
<androidx.core.widget.NestedScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:layout_behavior="@string/appbar_scrolling_view_behavior"
    android:background="@color/background">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:padding="16dp">

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Statistics"
            android:textSize="20sp"
            android:textStyle="bold"
            android:textColor="@color/black"
            android:layout_marginBottom="16dp"/>
            
        <ProgressBar
            android:id="@+id/progressBar"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="16dp"/>

        <GridLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:columnCount="2"
            android:alignmentMode="alignMargins"
            android:columnOrderPreserved="false">

            <!-- Categories Card -->
            <com.google.android.material.card.MaterialCardView
                android:id="@+id/cardCategories"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_columnWeight="1"
                android:layout_margin="8dp"
                app:cardCornerRadius="12dp"
                app:cardElevation="4dp"
                android:clickable="true"
                android:focusable="true"
                android:foreground="?android:attr/selectableItemBackground">
                
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:padding="16dp"
                    android:gravity="center">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Categories"
                        android:textSize="16sp"
                        android:textColor="@color/gray"/>
                    <TextView
                        android:id="@+id/tvTotalCategories"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="0"
                        android:textSize="24sp"
                        android:textStyle="bold"
                        android:textColor="@color/primary"/>
                </LinearLayout>
            </com.google.android.material.card.MaterialCardView>

            <!-- Products Card -->
            <com.google.android.material.card.MaterialCardView
                android:id="@+id/cardProducts"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_columnWeight="1"
                android:layout_margin="8dp"
                app:cardCornerRadius="12dp"
                app:cardElevation="4dp"
                android:clickable="true"
                android:focusable="true"
                android:foreground="?android:attr/selectableItemBackground">
                
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:padding="16dp"
                    android:gravity="center">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Products"
                        android:textSize="16sp"
                        android:textColor="@color/gray"/>
                    <TextView
                        android:id="@+id/tvTotalProducts"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="0"
                        android:textSize="24sp"
                        android:textStyle="bold"
                        android:textColor="@color/primary"/>
                </LinearLayout>
            </com.google.android.material.card.MaterialCardView>
            
            <!-- Users Card -->
            <com.google.android.material.card.MaterialCardView
                android:id="@+id/cardUsers"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_columnWeight="1"
                android:layout_margin="8dp"
                app:cardCornerRadius="12dp"
                app:cardElevation="4dp"
                android:clickable="true"
                android:focusable="true"
                android:foreground="?android:attr/selectableItemBackground">
                
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:padding="16dp"
                    android:gravity="center">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Users"
                        android:textSize="16sp"
                        android:textColor="@color/gray"/>
                    <TextView
                        android:id="@+id/tvTotalUsers"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="0"
                        android:textSize="24sp"
                        android:textStyle="bold"
                        android:textColor="@color/primary"/>
                    <TextView
                        android:id="@+id/tvActiveUsers"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Active: 0"
                        android:textSize="12sp"
                        android:textColor="@color/primary"/>
                    <TextView
                        android:id="@+id/tvBlockedUsers"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Blocked: 0"
                        android:textSize="12sp"
                        android:textColor="@color/error"/>
                </LinearLayout>
            </com.google.android.material.card.MaterialCardView>

            <!-- Orders Card -->
            <com.google.android.material.card.MaterialCardView
                android:id="@+id/cardOrders"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_columnWeight="1"
                android:layout_margin="8dp"
                app:cardCornerRadius="12dp"
                app:cardElevation="4dp"
                android:clickable="true"
                android:focusable="true"
                android:foreground="?android:attr/selectableItemBackground">
                
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:padding="16dp"
                    android:gravity="center">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Orders"
                        android:textSize="16sp"
                        android:textColor="@color/gray"/>
                    <TextView
                        android:id="@+id/tvTotalOrders"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="0"
                        android:textSize="24sp"
                        android:textStyle="bold"
                        android:textColor="@color/primary"/>
                    <TextView
                        android:id="@+id/tvPendingOrders"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Pending: 0"
                        android:textSize="12sp"
                        android:textColor="@color/gray"/>
                    <TextView
                        android:id="@+id/tvConfirmedOrders"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Confirmed: 0"
                        android:textSize="12sp"
                        android:textColor="@color/primary"/>
                    <TextView
                        android:id="@+id/tvDeliveredOrders"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Delivered: 0"
                        android:textSize="12sp"
                        android:textColor="@color/primary"/>
                    <TextView
                        android:id="@+id/tvCancelledOrders"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Cancelled: 0"
                        android:textSize="12sp"
                        android:textColor="@color/error"/>
                </LinearLayout>
            </com.google.android.material.card.MaterialCardView>
        </GridLayout>
        
        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Quick Actions"
            android:textSize="20sp"
            android:textStyle="bold"
            android:textColor="@color/black"
            android:layout_marginTop="24dp"
            android:layout_marginBottom="8dp"/>
            
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:weightSum="4">
            
            <Button
                android:id="@+id/btnQuickAddCategory"
                style="@style/Widget.MaterialComponents.Button.TextButton"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:text="Add Cat"/>
            <Button
                android:id="@+id/btnQuickAddProduct"
                style="@style/Widget.MaterialComponents.Button.TextButton"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:text="Add Prod"/>
            <Button
                android:id="@+id/btnQuickUsers"
                style="@style/Widget.MaterialComponents.Button.TextButton"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:text="Users"/>
            <Button
                android:id="@+id/btnQuickOrders"
                style="@style/Widget.MaterialComponents.Button.TextButton"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:text="Orders"/>
        </LinearLayout>

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Recent Orders"
            android:textSize="20sp"
            android:textStyle="bold"
            android:textColor="@color/black"
            android:layout_marginTop="24dp"
            android:layout_marginBottom="8dp"/>
            
        <androidx.recyclerview.widget.RecyclerView
            android:id="@+id/rvRecentOrders"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:nestedScrollingEnabled="false"/>
            
        <TextView
            android:id="@+id/tvNoRecentOrders"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="No recent orders."
            android:textAlignment="center"
            android:padding="24dp"
            android:visibility="gone"/>

    </LinearLayout>

</androidx.core.widget.NestedScrollView>
"""

with open(os.path.join(res_layout, "activity_dashboard.xml"), "w") as f: f.write(activity_dashboard)
with open(os.path.join(res_layout, "app_bar_dashboard.xml"), "w") as f: f.write(app_bar_dashboard)
with open(os.path.join(res_layout, "nav_header.xml"), "w") as f: f.write(nav_header)
with open(os.path.join(res_layout, "content_dashboard.xml"), "w") as f: f.write(content_dashboard)
with open(os.path.join(res_menu, "nav_menu.xml"), "w") as f: f.write(nav_menu)

print("Dashboard layouts generated.")
