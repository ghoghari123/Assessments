import os

res_layout = "f:/srushti/AdminApp/app/src/main/res/layout"
java_dir = "f:/srushti/AdminApp/app/src/main/java/com/example/adminapp"
models_dir = os.path.join(java_dir, "models")
adapters_dir = os.path.join(java_dir, "adapters")

activity_order = """<?xml version="1.0" encoding="utf-8"?>
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
            app:title="Manage Orders"
            app:titleTextColor="@color/white" />
            
        <HorizontalScrollView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:scrollbars="none"
            android:background="@color/white">
            <com.google.android.material.chip.ChipGroup
                android:id="@+id/chipGroupFilter"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:padding="8dp"
                app:singleSelection="true"
                app:selectionRequired="true">
                
                <com.google.android.material.chip.Chip
                    android:id="@+id/chipAll"
                    style="@style/Widget.MaterialComponents.Chip.Choice"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="All Orders"
                    android:checked="true"/>
                <com.google.android.material.chip.Chip
                    android:id="@+id/chipPending"
                    style="@style/Widget.MaterialComponents.Chip.Choice"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Pending"/>
                <com.google.android.material.chip.Chip
                    android:id="@+id/chipConfirmed"
                    style="@style/Widget.MaterialComponents.Chip.Choice"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Confirmed"/>
                <com.google.android.material.chip.Chip
                    android:id="@+id/chipDelivered"
                    style="@style/Widget.MaterialComponents.Chip.Choice"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Delivered"/>
                <com.google.android.material.chip.Chip
                    android:id="@+id/chipCancelled"
                    style="@style/Widget.MaterialComponents.Chip.Choice"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Cancelled"/>
                    
            </com.google.android.material.chip.ChipGroup>
        </HorizontalScrollView>
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
        android:text="No Orders Found"
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

item_order = """<?xml version="1.0" encoding="utf-8"?>
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
        android:orientation="vertical"
        android:padding="16dp">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal">

            <TextView
                android:id="@+id/tvOrderId"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:text="ID: #12345"
                android:textStyle="bold"
                android:textColor="@color/primary" />

            <TextView
                android:id="@+id/tvStatus"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Pending"
                android:textStyle="bold" />
        </LinearLayout>
        
        <View android:layout_width="match_parent" android:layout_height="1dp" android:background="@color/light_gray" android:layout_marginVertical="8dp"/>

        <TextView
            android:id="@+id/tvCustomerName"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Customer: John Doe"
            android:textColor="@color/black" />

        <TextView
            android:id="@+id/tvCustomerPhone"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Phone: 9876543210"
            android:textColor="@color/gray" />

        <TextView
            android:id="@+id/tvOrderDate"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Date: 12 Oct 2023"
            android:textColor="@color/gray" />

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:layout_marginTop="8dp">

            <TextView
                android:id="@+id/tvTotalItems"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:text="Items: 3"
                android:textColor="@color/gray" />

            <TextView
                android:id="@+id/tvTotalAmount"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="₹1500.0"
                android:textStyle="bold"
                android:textColor="@color/black" />
        </LinearLayout>

        <Button
            android:id="@+id/btnViewDetails"
            style="@style/Widget.MaterialComponents.Button.OutlinedButton"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="12dp"
            android:text="View Details" />

    </LinearLayout>
</com.google.android.material.card.MaterialCardView>
"""

activity_order_details = """<?xml version="1.0" encoding="utf-8"?>
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
            app:title="Order Details"
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
            android:padding="16dp">

            <com.google.android.material.card.MaterialCardView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginBottom="16dp"
                app:cardCornerRadius="12dp"
                app:cardElevation="2dp">

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:padding="16dp">
                    
                    <TextView android:id="@+id/tvOdId" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textStyle="bold" android:textColor="@color/primary"/>
                    <TextView android:id="@+id/tvOdDate" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="4dp"/>
                    <TextView android:id="@+id/tvOdStatus" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="4dp" android:textStyle="bold"/>
                    <TextView android:id="@+id/tvOdPayment" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="4dp"/>
                </LinearLayout>
            </com.google.android.material.card.MaterialCardView>

            <com.google.android.material.card.MaterialCardView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginBottom="16dp"
                app:cardCornerRadius="12dp"
                app:cardElevation="2dp">

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:padding="16dp">
                    
                    <TextView android:text="Customer Info" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textStyle="bold" android:textSize="16sp" android:layout_marginBottom="8dp"/>
                    <TextView android:id="@+id/tvOdName" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
                    <TextView android:id="@+id/tvOdPhone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="4dp"/>
                    <TextView android:id="@+id/tvOdAddress" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="4dp"/>
                </LinearLayout>
            </com.google.android.material.card.MaterialCardView>
            
            <com.google.android.material.card.MaterialCardView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginBottom="16dp"
                app:cardCornerRadius="12dp"
                app:cardElevation="2dp">

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:padding="16dp">
                    
                    <TextView android:text="Update Status" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textStyle="bold" android:textSize="16sp" android:layout_marginBottom="8dp"/>
                    <Spinner android:id="@+id/spinnerStatus" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="12dp"/>
                    <Button android:id="@+id/btnUpdateStatus" android:layout_width="match_parent" android:layout_height="wrap_content" android:text="Update Status"/>
                </LinearLayout>
            </com.google.android.material.card.MaterialCardView>

        </LinearLayout>
    </androidx.core.widget.NestedScrollView>

</androidx.coordinatorlayout.widget.CoordinatorLayout>
"""

order_model = """package com.example.adminapp.models

data class Order(
    var orderId: String = "",
    var customerName: String = "",
    var customerPhone: String = "",
    var deliveryAddress: String = "",
    var orderDate: Long = 0,
    var totalProducts: Int = 0,
    var totalAmount: Double = 0.0,
    var paymentMethod: String = "Cash on Delivery",
    var status: String = "Pending"
)
"""

order_adapter = """package com.example.adminapp.adapters

import android.graphics.Color
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.adminapp.R
import com.example.adminapp.models.Order
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class OrderAdapter(
    private var orderList: List<Order>,
    private val onViewDetailsClick: (Order) -> Unit
) : RecyclerView.Adapter<OrderAdapter.OrderViewHolder>() {

    class OrderViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val tvOrderId: TextView = itemView.findViewById(R.id.tvOrderId)
        val tvStatus: TextView = itemView.findViewById(R.id.tvStatus)
        val tvCustomerName: TextView = itemView.findViewById(R.id.tvCustomerName)
        val tvCustomerPhone: TextView = itemView.findViewById(R.id.tvCustomerPhone)
        val tvOrderDate: TextView = itemView.findViewById(R.id.tvOrderDate)
        val tvTotalItems: TextView = itemView.findViewById(R.id.tvTotalItems)
        val tvTotalAmount: TextView = itemView.findViewById(R.id.tvTotalAmount)
        val btnViewDetails: Button = itemView.findViewById(R.id.btnViewDetails)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): OrderViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.id.item_order, parent, false)
        return OrderViewHolder(view)
    }

    override fun onBindViewHolder(holder: OrderViewHolder, position: Int) {
        val order = orderList[position]
        holder.tvOrderId.text = "ID: ${order.orderId}"
        holder.tvCustomerName.text = "Customer: ${order.customerName}"
        holder.tvCustomerPhone.text = "Phone: ${order.customerPhone}"
        
        val sdf = SimpleDateFormat("dd MMM yyyy", Locale.getDefault())
        holder.tvOrderDate.text = "Date: ${sdf.format(Date(order.orderDate))}"
        
        holder.tvTotalItems.text = "Items: ${order.totalProducts}"
        holder.tvTotalAmount.text = "₹${order.totalAmount}"
        
        holder.tvStatus.text = order.status
        when (order.status) {
            "Pending" -> holder.tvStatus.setTextColor(Color.parseColor("#FFA500"))
            "Confirmed" -> holder.tvStatus.setTextColor(Color.parseColor("#2196F3"))
            "Delivered" -> holder.tvStatus.setTextColor(Color.parseColor("#4CAF50"))
            "Cancelled" -> holder.tvStatus.setTextColor(Color.RED)
            else -> holder.tvStatus.setTextColor(Color.BLACK)
        }
        
        holder.btnViewDetails.setOnClickListener { onViewDetailsClick(order) }
    }

    override fun getItemCount() = orderList.size
    
    fun updateList(newList: List<Order>) {
        orderList = newList
        notifyDataSetChanged()
    }
}
"""

order_activity = """package com.example.adminapp

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.SearchView
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.adminapp.adapters.OrderAdapter
import com.example.adminapp.databinding.ActivityOrderBinding
import com.example.adminapp.models.Order
import com.google.android.material.chip.Chip
import com.google.firebase.firestore.FirebaseFirestore
import java.util.*

class OrderActivity : AppCompatActivity() {

    private lateinit var binding: ActivityOrderBinding
    private lateinit var firestore: FirebaseFirestore
    private lateinit var adapter: OrderAdapter
    
    private var orderList = mutableListOf<Order>()
    private var filteredList = mutableListOf<Order>()
    private var currentFilter = "All Orders"
    private var currentQuery = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityOrderBinding.inflate(layoutInflater)
        setContentView(binding.root)

        firestore = FirebaseFirestore.getInstance()

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        setupRecyclerView()
        setupFilters()
        loadOrders()
    }

    private fun setupRecyclerView() {
        adapter = OrderAdapter(filteredList) { order ->
            val intent = Intent(this, OrderDetailsActivity::class.java)
            intent.putExtra("ORDER_ID", order.orderId)
            startActivity(intent)
        }
        binding.recyclerView.layoutManager = LinearLayoutManager(this)
        binding.recyclerView.adapter = adapter
    }

    private fun setupFilters() {
        binding.chipGroupFilter.setOnCheckedStateChangeListener { group, checkedIds ->
            if (checkedIds.isNotEmpty()) {
                val chip = findViewById<Chip>(checkedIds[0])
                currentFilter = chip.text.toString()
                applyFilters()
            }
        }
    }

    private fun loadOrders() {
        binding.progressBar.visibility = View.VISIBLE
        firestore.collection("orders").addSnapshotListener { snapshot, error ->
            binding.progressBar.visibility = View.GONE
            if (error != null) {
                Toast.makeText(this, "Failed to load: ${error.message}", Toast.LENGTH_SHORT).show()
                return@addSnapshotListener
            }
            
            orderList.clear()
            snapshot?.let {
                for (doc in it) {
                    val order = doc.toObject(Order::class.java)
                    orderList.add(order)
                }
            }
            // Sort by date descending
            orderList.sortByDescending { it.orderDate }
            applyFilters()
        }
    }

    private fun applyFilters() {
        filteredList.clear()
        
        for (order in orderList) {
            val matchesFilter = currentFilter == "All Orders" || order.status == currentFilter
            
            val matchesQuery = if (currentQuery.isEmpty()) {
                true
            } else {
                val lowerCaseQuery = currentQuery.lowercase(Locale.getDefault())
                order.orderId.lowercase(Locale.getDefault()).contains(lowerCaseQuery) ||
                order.customerName.lowercase(Locale.getDefault()).contains(lowerCaseQuery) ||
                order.customerPhone.contains(lowerCaseQuery)
            }
            
            if (matchesFilter && matchesQuery) {
                filteredList.add(order)
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
                currentQuery = newText ?: ""
                applyFilters()
                return true
            }
        })
        return super.onPrepareOptionsMenu(menu)
    }
}
"""

order_details_activity = """package com.example.adminapp

import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.adminapp.databinding.ActivityOrderDetailsBinding
import com.example.adminapp.models.Order
import com.google.firebase.firestore.FirebaseFirestore
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class OrderDetailsActivity : AppCompatActivity() {

    private lateinit var binding: ActivityOrderDetailsBinding
    private lateinit var firestore: FirebaseFirestore
    private var currentOrderId: String? = null
    
    private val statuses = arrayOf("Pending", "Confirmed", "Delivered", "Cancelled")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityOrderDetailsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        firestore = FirebaseFirestore.getInstance()

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, statuses)
        binding.spinnerStatus.adapter = adapter

        currentOrderId = intent.getStringExtra("ORDER_ID")
        if (currentOrderId != null) {
            loadOrderDetails(currentOrderId!!)
        } else {
            Toast.makeText(this, "Order ID missing", Toast.LENGTH_SHORT).show()
            finish()
        }
        
        binding.btnUpdateStatus.setOnClickListener {
            updateOrderStatus()
        }
    }

    private fun loadOrderDetails(orderId: String) {
        firestore.collection("orders").document(orderId).get()
            .addOnSuccessListener { doc ->
                if (doc.exists()) {
                    val order = doc.toObject(Order::class.java)
                    order?.let { displayOrderDetails(it) }
                }
            }
            .addOnFailureListener { e ->
                Toast.makeText(this, "Error: ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    private fun displayOrderDetails(order: Order) {
        binding.tvOdId.text = "Order ID: ${order.orderId}"
        val sdf = SimpleDateFormat("dd MMM yyyy, HH:mm", Locale.getDefault())
        binding.tvOdDate.text = "Date: ${sdf.format(Date(order.orderDate))}"
        binding.tvOdStatus.text = "Status: ${order.status}"
        binding.tvOdPayment.text = "Payment: ${order.paymentMethod}"
        
        binding.tvOdName.text = "Name: ${order.customerName}"
        binding.tvOdPhone.text = "Phone: ${order.customerPhone}"
        binding.tvOdAddress.text = "Address: ${order.deliveryAddress}"
        
        val spinnerPos = statuses.indexOf(order.status)
        if (spinnerPos >= 0) binding.spinnerStatus.setSelection(spinnerPos)
    }
    
    private fun updateOrderStatus() {
        val newStatus = binding.spinnerStatus.selectedItem.toString()
        if (currentOrderId != null) {
            firestore.collection("orders").document(currentOrderId!!).update("status", newStatus)
                .addOnSuccessListener {
                    Toast.makeText(this, "Order Status Updated Successfully", Toast.LENGTH_SHORT).show()
                    binding.tvOdStatus.text = "Status: $newStatus"
                }
                .addOnFailureListener { e ->
                    Toast.makeText(this, "Failed: ${e.message}", Toast.LENGTH_SHORT).show()
                }
        }
    }
}
"""

with open(os.path.join(res_layout, "activity_order.xml"), "w", encoding="utf-8") as f: f.write(activity_order)
with open(os.path.join(res_layout, "item_order.xml"), "w", encoding="utf-8") as f: f.write(item_order)
with open(os.path.join(res_layout, "activity_order_details.xml"), "w", encoding="utf-8") as f: f.write(activity_order_details)

with open(os.path.join(models_dir, "Order.kt"), "w", encoding="utf-8") as f: f.write(order_model)
with open(os.path.join(adapters_dir, "OrderAdapter.kt"), "w", encoding="utf-8") as f: f.write(order_adapter)
with open(os.path.join(java_dir, "OrderActivity.kt"), "w", encoding="utf-8") as f: f.write(order_activity)
with open(os.path.join(java_dir, "OrderDetailsActivity.kt"), "w", encoding="utf-8") as f: f.write(order_details_activity)

print("Order module generated.")
