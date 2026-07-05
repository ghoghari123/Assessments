package com.example.adminapp

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
