package com.example.adminapp

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
