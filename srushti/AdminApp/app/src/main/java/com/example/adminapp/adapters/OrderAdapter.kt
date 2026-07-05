package com.example.adminapp.adapters

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
