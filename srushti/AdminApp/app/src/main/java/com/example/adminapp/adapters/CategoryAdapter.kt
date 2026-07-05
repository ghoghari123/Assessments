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
import com.example.adminapp.models.Category

class CategoryAdapter(
    private var categoryList: List<Category>,
    private val onEditClick: (Category) -> Unit,
    private val onDeleteClick: (Category) -> Unit
) : RecyclerView.Adapter<CategoryAdapter.CategoryViewHolder>() {

    class CategoryViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val ivCategory: ImageView = itemView.findViewById(R.id.ivCategory)
        val tvCategoryName: TextView = itemView.findViewById(R.id.tvCategoryName)
        val btnEdit: ImageButton = itemView.findViewById(R.id.btnEdit)
        val btnDelete: ImageButton = itemView.findViewById(R.id.btnDelete)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CategoryViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.id.item_category, parent, false)
        return CategoryViewHolder(view)
    }

    override fun onBindViewHolder(holder: CategoryViewHolder, position: Int) {
        val category = categoryList[position]
        holder.tvCategoryName.text = category.categoryName
        Glide.with(holder.itemView.context).load(category.categoryImage).into(holder.ivCategory)
        
        holder.btnEdit.setOnClickListener { onEditClick(category) }
        holder.btnDelete.setOnClickListener { onDeleteClick(category) }
    }

    override fun getItemCount() = categoryList.size
    
    fun updateList(newList: List<Category>) {
        categoryList = newList
        notifyDataSetChanged()
    }
}
