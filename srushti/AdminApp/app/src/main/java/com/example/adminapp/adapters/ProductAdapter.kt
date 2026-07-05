package com.example.adminapp.adapters

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageButton
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.adminapp.R
import com.example.adminapp.models.Product

class ProductAdapter(
    private var productList: List<Product>,
    private val onEditClick: (Product) -> Unit,
    private val onDeleteClick: (Product) -> Unit
) : RecyclerView.Adapter<ProductAdapter.ProductViewHolder>() {

    class ProductViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val ivProduct: ImageView = itemView.findViewById(R.id.ivProduct)
        val tvProductName: TextView = itemView.findViewById(R.id.tvProductName)
        val tvCategoryName: TextView = itemView.findViewById(R.id.tvCategoryName)
        val tvPriceInfo: TextView = itemView.findViewById(R.id.tvPriceInfo)
        val tvStock: TextView = itemView.findViewById(R.id.tvStock)
        val btnEdit: ImageButton = itemView.findViewById(R.id.btnEdit)
        val btnDelete: ImageButton = itemView.findViewById(R.id.btnDelete)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ProductViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.id.item_product, parent, false)
        return ProductViewHolder(view)
    }

    override fun onBindViewHolder(holder: ProductViewHolder, position: Int) {
        val product = productList[position]
        holder.tvProductName.text = product.productName
        holder.tvCategoryName.text = product.categoryName
        holder.tvPriceInfo.text = "₹${product.finalPrice} (${product.discount}% off)"
        holder.tvStock.text = "Stock: ${product.stock}"
        
        Glide.with(holder.itemView.context).load(product.productImage).into(holder.ivProduct)
        
        holder.btnEdit.setOnClickListener { onEditClick(product) }
        holder.btnDelete.setOnClickListener { onDeleteClick(product) }
    }

    override fun getItemCount() = productList.size
    
    fun updateList(newList: List<Product>) {
        productList = newList
        notifyDataSetChanged()
    }
}
