import os

dashboard_kt_updated = """package com.example.adminapp

import android.content.Intent
import android.os.Bundle
import android.view.MenuItem
import android.view.View
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.GravityCompat
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.adminapp.adapters.OrderAdapter
import com.example.adminapp.databinding.ActivityDashboardBinding
import com.example.adminapp.models.Order
import com.google.android.material.navigation.NavigationView
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.Query

class DashboardActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {

    private lateinit var binding: ActivityDashboardBinding
    private lateinit var auth: FirebaseAuth
    private lateinit var firestore: FirebaseFirestore
    private lateinit var recentOrdersAdapter: OrderAdapter
    private var recentOrdersList = mutableListOf<Order>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDashboardBinding.inflate(layoutInflater)
        setContentView(binding.root)

        auth = FirebaseAuth.getInstance()
        firestore = FirebaseFirestore.getInstance()

        // Setup Toolbar
        setSupportActionBar(binding.appBar.toolbar)
        
        // Setup Drawer
        val toggle = ActionBarDrawerToggle(
            this, binding.drawerLayout, binding.appBar.toolbar,
            R.string.app_name, R.string.app_name
        )
        binding.drawerLayout.addDrawerListener(toggle)
        toggle.syncState()

        binding.navigationView.setNavigationItemSelectedListener(this)

        setupClickListeners()
        setupRecentOrdersRecyclerView()
        loadDashboardData()
    }

    private fun setupRecentOrdersRecyclerView() {
        recentOrdersAdapter = OrderAdapter(recentOrdersList) { order ->
            val intent = Intent(this, OrderDetailsActivity::class.java)
            intent.putExtra("ORDER_ID", order.orderId)
            startActivity(intent)
        }
        binding.appBar.rvRecentOrders.layoutManager = LinearLayoutManager(this)
        binding.appBar.rvRecentOrders.adapter = recentOrdersAdapter
    }

    private fun setupClickListeners() {
        binding.appBar.cardCategories.setOnClickListener { startActivity(Intent(this, CategoryActivity::class.java)) }
        binding.appBar.cardProducts.setOnClickListener { startActivity(Intent(this, ProductActivity::class.java)) }
        binding.appBar.cardUsers.setOnClickListener { startActivity(Intent(this, UserActivity::class.java)) }
        binding.appBar.cardOrders.setOnClickListener { startActivity(Intent(this, OrderActivity::class.java)) }
        
        binding.appBar.btnQuickAddCategory.setOnClickListener { startActivity(Intent(this, CategoryActivity::class.java)) }
        binding.appBar.btnQuickAddProduct.setOnClickListener { startActivity(Intent(this, ProductActivity::class.java)) }
        binding.appBar.btnQuickUsers.setOnClickListener { startActivity(Intent(this, UserActivity::class.java)) }
        binding.appBar.btnQuickOrders.setOnClickListener { startActivity(Intent(this, OrderActivity::class.java)) }
    }

    private fun loadDashboardData() {
        binding.appBar.progressBar.visibility = View.VISIBLE
        
        // Categories
        firestore.collection("categories").addSnapshotListener { value, error ->
            if (error == null && value != null) {
                binding.appBar.tvTotalCategories.text = value.size().toString()
            }
        }
        
        // Products
        firestore.collection("products").addSnapshotListener { value, error ->
            if (error == null && value != null) {
                binding.appBar.tvTotalProducts.text = value.size().toString()
            }
        }
        
        // Users
        firestore.collection("users").whereEqualTo("role", "User").addSnapshotListener { value, error ->
            if (error == null && value != null) {
                var active = 0
                var blocked = 0
                for (doc in value) {
                    val status = doc.getString("status") ?: "Active"
                    if (status == "Blocked") blocked++ else active++
                }
                binding.appBar.tvTotalUsers.text = value.size().toString()
                binding.appBar.tvActiveUsers.text = "Active: $active"
                binding.appBar.tvBlockedUsers.text = "Blocked: $blocked"
            }
        }
        
        // Orders
        firestore.collection("orders").addSnapshotListener { value, error ->
            if (error == null && value != null) {
                var pending = 0
                var confirmed = 0
                var delivered = 0
                var cancelled = 0
                
                for (doc in value) {
                    val status = doc.getString("status") ?: "Pending"
                    when (status) {
                        "Pending" -> pending++
                        "Confirmed" -> confirmed++
                        "Delivered" -> delivered++
                        "Cancelled" -> cancelled++
                    }
                }
                
                binding.appBar.tvTotalOrders.text = value.size().toString()
                binding.appBar.tvPendingOrders.text = "Pending: $pending"
                binding.appBar.tvConfirmedOrders.text = "Confirmed: $confirmed"
                binding.appBar.tvDeliveredOrders.text = "Delivered: $delivered"
                binding.appBar.tvCancelledOrders.text = "Cancelled: $cancelled"
                
                binding.appBar.progressBar.visibility = View.GONE
            }
        }
        
        // Recent Orders
        firestore.collection("orders").orderBy("orderDate", Query.Direction.DESCENDING).limit(5).addSnapshotListener { value, error ->
            if (error == null && value != null) {
                recentOrdersList.clear()
                for (doc in value) {
                    recentOrdersList.add(doc.toObject(Order::class.java))
                }
                if (recentOrdersList.isEmpty()) {
                    binding.appBar.tvNoRecentOrders.visibility = View.VISIBLE
                    binding.appBar.rvRecentOrders.visibility = View.GONE
                } else {
                    binding.appBar.tvNoRecentOrders.visibility = View.GONE
                    binding.appBar.rvRecentOrders.visibility = View.VISIBLE
                }
                recentOrdersAdapter.updateList(recentOrdersList)
            }
        }
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.nav_dashboard -> { /* Already here */ }
            R.id.nav_categories -> startActivity(Intent(this, CategoryActivity::class.java))
            R.id.nav_products -> startActivity(Intent(this, ProductActivity::class.java))
            R.id.nav_users -> startActivity(Intent(this, UserActivity::class.java))
            R.id.nav_orders -> startActivity(Intent(this, OrderActivity::class.java))
            R.id.nav_logout -> showLogoutDialog()
        }
        binding.drawerLayout.closeDrawer(GravityCompat.START)
        return true
    }

    private fun showLogoutDialog() {
        AlertDialog.Builder(this)
            .setTitle("Logout")
            .setMessage("Are you sure you want to logout?")
            .setPositiveButton("Yes") { _, _ ->
                auth.signOut()
                val intent = Intent(this, LoginActivity::class.java)
                intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
                startActivity(intent)
                finish()
            }
            .setNegativeButton("No", null)
            .show()
    }

    override fun onBackPressed() {
        if (binding.drawerLayout.isDrawerOpen(GravityCompat.START)) {
            binding.drawerLayout.closeDrawer(GravityCompat.START)
        } else {
            super.onBackPressed()
        }
    }
}
"""
with open("f:/srushti/AdminApp/app/src/main/java/com/example/adminapp/DashboardActivity.kt", "w", encoding="utf-8") as f: f.write(dashboard_kt_updated)
print("Dashboard updated.")
