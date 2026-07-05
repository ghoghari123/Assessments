import os

res_layout = "f:/srushti/AdminApp/app/src/main/res/layout"
java_dir = "f:/srushti/AdminApp/app/src/main/java/com/example/adminapp"
models_dir = os.path.join(java_dir, "models")
adapters_dir = os.path.join(java_dir, "adapters")

activity_user = """<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/background">

    <com.google.android.material.appbar.AppBarLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
        <androidx.appcompat.widget.Toolbar
            android:id="@+id/toolbar"
            android:layout_width="match_parent"
            android:layout_height="?attr/actionBarSize"
            android:background="?attr/colorPrimary"
            app:title="Manage Users"
            app:titleTextColor="@color/white" />
    </com.google.android.material.appbar.AppBarLayout>

    <ProgressBar
        android:id="@+id/progressBar"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:visibility="gone" />

    <TextView
        android:id="@+id/tvEmpty"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:text="No Users Found"
        android:visibility="gone" />

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:layout_behavior="@string/appbar_scrolling_view_behavior"
        android:padding="8dp"
        android:clipToPadding="false" />

</androidx.coordinatorlayout.widget.CoordinatorLayout>
"""

item_user = """<?xml version="1.0" encoding="utf-8"?>
<com.google.android.material.card.MaterialCardView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_margin="8dp"
    app:cardCornerRadius="12dp"
    app:cardElevation="4dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:padding="12dp"
        android:gravity="center_vertical">

        <de.hdodenhof.circleimageview.CircleImageView
            android:id="@+id/ivProfile"
            android:layout_width="60dp"
            android:layout_height="60dp"
            android:src="@mipmap/ic_launcher_round"
            app:civ_border_width="2dp"
            app:civ_border_color="@color/gray"/>

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:layout_marginStart="12dp"
            android:orientation="vertical">

            <TextView
                android:id="@+id/tvFullName"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="16sp"
                android:textStyle="bold"
                android:textColor="@color/black" />

            <TextView
                android:id="@+id/tvEmail"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="14sp"
                android:textColor="@color/gray" />

            <TextView
                android:id="@+id/tvMobile"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="14sp"
                android:textColor="@color/gray" />

            <TextView
                android:id="@+id/tvStatus"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="14sp"
                android:textStyle="bold" />
        </LinearLayout>

        <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:gravity="center">

            <Button
                android:id="@+id/btnView"
                style="@style/Widget.MaterialComponents.Button.TextButton"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="View"
                android:textColor="@color/primary"/>

            <Button
                android:id="@+id/btnBlock"
                style="@style/Widget.MaterialComponents.Button.TextButton"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Block"
                android:textColor="@color/error"/>
        </LinearLayout>
    </LinearLayout>
</com.google.android.material.card.MaterialCardView>
"""

activity_user_details = """<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/background">

    <com.google.android.material.appbar.AppBarLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
        <androidx.appcompat.widget.Toolbar
            android:id="@+id/toolbar"
            android:layout_width="match_parent"
            android:layout_height="?attr/actionBarSize"
            android:background="?attr/colorPrimary"
            app:title="User Details"
            app:titleTextColor="@color/white" />
    </com.google.android.material.appbar.AppBarLayout>

    <androidx.core.widget.NestedScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:layout_behavior="@string/appbar_scrolling_view_behavior">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="24dp"
            android:gravity="center_horizontal">

            <de.hdodenhof.circleimageview.CircleImageView
                android:id="@+id/ivProfileDetails"
                android:layout_width="120dp"
                android:layout_height="120dp"
                android:src="@mipmap/ic_launcher_round"
                android:layout_marginBottom="24dp"
                app:civ_border_width="2dp"
                app:civ_border_color="@color/primary"/>

            <com.google.android.material.card.MaterialCardView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                app:cardCornerRadius="12dp"
                app:cardElevation="4dp">

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:padding="16dp">

                    <TextView android:id="@+id/tvDetName" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textSize="18sp" android:textStyle="bold" android:layout_marginBottom="8dp"/>
                    <TextView android:id="@+id/tvDetEmail" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="8dp"/>
                    <TextView android:id="@+id/tvDetMobile" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="8dp"/>
                    <TextView android:id="@+id/tvDetGender" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="8dp"/>
                    <TextView android:id="@+id/tvDetAddress" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="8dp"/>
                    <TextView android:id="@+id/tvDetRegDate" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="8dp"/>
                    
                    <View android:layout_width="match_parent" android:layout_height="1dp" android:background="@color/light_gray" android:layout_marginVertical="12dp"/>
                    
                    <TextView android:id="@+id/tvDetOrders" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="8dp"/>
                    <TextView android:id="@+id/tvDetStatus" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="8dp" android:textStyle="bold"/>

                </LinearLayout>
            </com.google.android.material.card.MaterialCardView>
        </LinearLayout>
    </androidx.core.widget.NestedScrollView>

</androidx.coordinatorlayout.widget.CoordinatorLayout>
"""

user_model = """package com.example.adminapp.models

data class User(
    var userId: String = "",
    var fullName: String = "",
    var email: String = "",
    var mobile: String = "",
    var gender: String = "",
    var address: String = "",
    var profileImage: String = "",
    var role: String = "User",
    var status: String = "Active",
    var createdAt: Long = 0,
    var totalOrders: Int = 0
)
"""

user_adapter = """package com.example.adminapp.adapters

import android.graphics.Color
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.adminapp.R
import com.example.adminapp.models.User
import de.hdodenhof.circleimageview.CircleImageView
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class UserAdapter(
    private var userList: List<User>,
    private val onViewClick: (User) -> Unit,
    private val onBlockClick: (User) -> Unit
) : RecyclerView.Adapter<UserAdapter.UserViewHolder>() {

    class UserViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val ivProfile: CircleImageView = itemView.findViewById(R.id.ivProfile)
        val tvFullName: TextView = itemView.findViewById(R.id.tvFullName)
        val tvEmail: TextView = itemView.findViewById(R.id.tvEmail)
        val tvMobile: TextView = itemView.findViewById(R.id.tvMobile)
        val tvStatus: TextView = itemView.findViewById(R.id.tvStatus)
        val btnView: Button = itemView.findViewById(R.id.btnView)
        val btnBlock: Button = itemView.findViewById(R.id.btnBlock)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.id.item_user, parent, false)
        return UserViewHolder(view)
    }

    override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
        val user = userList[position]
        holder.tvFullName.text = user.fullName
        holder.tvEmail.text = user.email
        holder.tvMobile.text = user.mobile
        
        if (user.status == "Blocked") {
            holder.tvStatus.text = "Blocked"
            holder.tvStatus.setTextColor(Color.RED)
            holder.btnBlock.text = "Unblock"
            holder.btnBlock.setTextColor(Color.parseColor("#4CAF50"))
        } else {
            holder.tvStatus.text = "Active"
            holder.tvStatus.setTextColor(Color.parseColor("#4CAF50"))
            holder.btnBlock.text = "Block"
            holder.btnBlock.setTextColor(Color.RED)
        }
        
        if (user.profileImage.isNotEmpty()) {
            Glide.with(holder.itemView.context).load(user.profileImage).into(holder.ivProfile)
        } else {
            holder.ivProfile.setImageResource(R.mipmap.ic_launcher_round)
        }
        
        holder.btnView.setOnClickListener { onViewClick(user) }
        holder.btnBlock.setOnClickListener { onBlockClick(user) }
    }

    override fun getItemCount() = userList.size
    
    fun updateList(newList: List<User>) {
        userList = newList
        notifyDataSetChanged()
    }
}
"""

user_activity = """package com.example.adminapp

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.SearchView
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.adminapp.adapters.UserAdapter
import com.example.adminapp.databinding.ActivityUserBinding
import com.example.adminapp.models.User
import com.google.firebase.firestore.FirebaseFirestore
import java.util.*

class UserActivity : AppCompatActivity() {

    private lateinit var binding: ActivityUserBinding
    private lateinit var firestore: FirebaseFirestore
    private lateinit var adapter: UserAdapter
    
    private var userList = mutableListOf<User>()
    private var filteredList = mutableListOf<User>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityUserBinding.inflate(layoutInflater)
        setContentView(binding.root)

        firestore = FirebaseFirestore.getInstance()

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        setupRecyclerView()
        loadUsers()
    }

    private fun setupRecyclerView() {
        adapter = UserAdapter(filteredList, { user ->
            val intent = Intent(this, UserDetailsActivity::class.java)
            intent.putExtra("USER_ID", user.userId)
            startActivity(intent)
        }, { user ->
            toggleUserStatus(user)
        })
        binding.recyclerView.layoutManager = LinearLayoutManager(this)
        binding.recyclerView.adapter = adapter
    }

    private fun loadUsers() {
        binding.progressBar.visibility = View.VISIBLE
        firestore.collection("users").whereEqualTo("role", "User").addSnapshotListener { snapshot, error ->
            binding.progressBar.visibility = View.GONE
            if (error != null) {
                Toast.makeText(this, "Failed to load: ${error.message}", Toast.LENGTH_SHORT).show()
                return@addSnapshotListener
            }
            
            userList.clear()
            snapshot?.let {
                for (doc in it) {
                    val user = doc.toObject(User::class.java)
                    user.userId = doc.id
                    userList.add(user)
                }
            }
            filterList("")
        }
    }

    private fun filterList(query: String) {
        filteredList.clear()
        if (query.isEmpty()) {
            filteredList.addAll(userList)
        } else {
            val lowerCaseQuery = query.lowercase(Locale.getDefault())
            for (user in userList) {
                if (user.fullName.lowercase(Locale.getDefault()).contains(lowerCaseQuery) ||
                    user.email.lowercase(Locale.getDefault()).contains(lowerCaseQuery) ||
                    user.mobile.contains(lowerCaseQuery)) {
                    filteredList.add(user)
                }
            }
        }
        
        if (filteredList.isEmpty()) {
            binding.tvEmpty.visibility = View.VISIBLE
        } else {
            binding.tvEmpty.visibility = View.GONE
        }
        
        adapter.updateList(filteredList)
    }
    
    override fun onPrepareOptionsMenu(menu: Menu?): Boolean {
        menu?.clear()
        val searchItem = menu?.add(Menu.NONE, 1001, Menu.NONE, "Search")
        searchItem?.setIcon(android.R.drawable.ic_menu_search)
        searchItem?.setShowAsAction(Menu.SHOW_AS_ACTION_ALWAYS or Menu.SHOW_AS_ACTION_COLLAPSE_ACTION_VIEW)
        val searchView = SearchView(this)
        searchItem?.actionView = searchView
        
        searchView.setOnQueryTextListener(object : SearchView.OnQueryTextListener {
            override fun onQueryTextSubmit(query: String?): Boolean = false
            override fun onQueryTextChange(newText: String?): Boolean {
                filterList(newText ?: "")
                return true
            }
        })
        return super.onPrepareOptionsMenu(menu)
    }

    private fun toggleUserStatus(user: User) {
        val newStatus = if (user.status == "Blocked") "Active" else "Blocked"
        val message = if (newStatus == "Blocked") "Are you sure you want to block this user?" else "Are you sure you want to unblock this user?"
        
        AlertDialog.Builder(this)
            .setTitle("$newStatus User")
            .setMessage(message)
            .setPositiveButton("Yes") { _, _ ->
                binding.progressBar.visibility = View.VISIBLE
                firestore.collection("users").document(user.userId).update("status", newStatus)
                    .addOnSuccessListener {
                        binding.progressBar.visibility = View.GONE
                        Toast.makeText(this, "User $newStatus Successfully", Toast.LENGTH_SHORT).show()
                    }
                    .addOnFailureListener { e ->
                        binding.progressBar.visibility = View.GONE
                        Toast.makeText(this, "Failed: ${e.message}", Toast.LENGTH_SHORT).show()
                    }
            }
            .setNegativeButton("No", null)
            .show()
    }
}
"""

user_details_activity = """package com.example.adminapp

import android.graphics.Color
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide
import com.example.adminapp.databinding.ActivityUserDetailsBinding
import com.example.adminapp.models.User
import com.google.firebase.firestore.FirebaseFirestore
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class UserDetailsActivity : AppCompatActivity() {

    private lateinit var binding: ActivityUserDetailsBinding
    private lateinit var firestore: FirebaseFirestore

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityUserDetailsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        firestore = FirebaseFirestore.getInstance()

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        val userId = intent.getStringExtra("USER_ID")
        if (userId != null) {
            loadUserDetails(userId)
        } else {
            Toast.makeText(this, "User ID missing", Toast.LENGTH_SHORT).show()
            finish()
        }
    }

    private fun loadUserDetails(userId: String) {
        firestore.collection("users").document(userId).get()
            .addOnSuccessListener { doc ->
                if (doc.exists()) {
                    val user = doc.toObject(User::class.java)
                    user?.let { displayUserDetails(it) }
                }
            }
            .addOnFailureListener { e ->
                Toast.makeText(this, "Error: ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    private fun displayUserDetails(user: User) {
        binding.tvDetName.text = "Name: ${user.fullName}"
        binding.tvDetEmail.text = "Email: ${user.email}"
        binding.tvDetMobile.text = "Mobile: ${user.mobile}"
        binding.tvDetGender.text = "Gender: ${if (user.gender.isEmpty()) "N/A" else user.gender}"
        binding.tvDetAddress.text = "Address: ${if (user.address.isEmpty()) "N/A" else user.address}"
        
        val sdf = SimpleDateFormat("dd MMM yyyy, HH:mm", Locale.getDefault())
        val dateStr = if (user.createdAt > 0) sdf.format(Date(user.createdAt)) else "N/A"
        binding.tvDetRegDate.text = "Registered: $dateStr"
        
        binding.tvDetOrders.text = "Total Orders: ${user.totalOrders}"
        
        binding.tvDetStatus.text = "Status: ${user.status}"
        if (user.status == "Blocked") {
            binding.tvDetStatus.setTextColor(Color.RED)
        } else {
            binding.tvDetStatus.setTextColor(Color.parseColor("#4CAF50"))
        }

        if (user.profileImage.isNotEmpty()) {
            Glide.with(this).load(user.profileImage).into(binding.ivProfileDetails)
        }
    }
}
"""

with open(os.path.join(res_layout, "activity_user.xml"), "w", encoding="utf-8") as f: f.write(activity_user)
with open(os.path.join(res_layout, "item_user.xml"), "w", encoding="utf-8") as f: f.write(item_user)
with open(os.path.join(res_layout, "activity_user_details.xml"), "w", encoding="utf-8") as f: f.write(activity_user_details)

with open(os.path.join(models_dir, "User.kt"), "w", encoding="utf-8") as f: f.write(user_model)
with open(os.path.join(adapters_dir, "UserAdapter.kt"), "w", encoding="utf-8") as f: f.write(user_adapter)
with open(os.path.join(java_dir, "UserActivity.kt"), "w", encoding="utf-8") as f: f.write(user_activity)
with open(os.path.join(java_dir, "UserDetailsActivity.kt"), "w", encoding="utf-8") as f: f.write(user_details_activity)

print("User module generated.")
