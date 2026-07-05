import os

res_layout = "f:/srushti/AdminApp/app/src/main/res/layout"
java_dir = "f:/srushti/AdminApp/app/src/main/java/com/example/adminapp"
models_dir = os.path.join(java_dir, "models")
adapters_dir = os.path.join(java_dir, "adapters")

# Layouts
activity_category = """<?xml version="1.0" encoding="utf-8"?>
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
            app:title="Manage Categories"
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
        android:text="No Categories Found"
        android:visibility="gone" />

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:layout_behavior="@string/appbar_scrolling_view_behavior"
        android:padding="8dp"
        android:clipToPadding="false" />

    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/fabAdd"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="bottom|end"
        android:layout_margin="16dp"
        android:src="@android:drawable/ic_input_add"
        app:tint="@color/white" />

</androidx.coordinatorlayout.widget.CoordinatorLayout>
"""

item_category = """<?xml version="1.0" encoding="utf-8"?>
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

        <ImageView
            android:id="@+id/ivCategory"
            android:layout_width="60dp"
            android:layout_height="60dp"
            android:scaleType="centerCrop"
            android:background="#EEEEEE" />

        <TextView
            android:id="@+id/tvCategoryName"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:layout_marginStart="16dp"
            android:textSize="18sp"
            android:textStyle="bold"
            android:textColor="@color/black" />

        <ImageButton
            android:id="@+id/btnEdit"
            android:layout_width="40dp"
            android:layout_height="40dp"
            android:background="?attr/selectableItemBackgroundBorderless"
            android:src="@android:drawable/ic_menu_edit"
            app:tint="@color/primary" />

        <ImageButton
            android:id="@+id/btnDelete"
            android:layout_width="40dp"
            android:layout_height="40dp"
            android:background="?attr/selectableItemBackgroundBorderless"
            android:src="@android:drawable/ic_menu_delete"
            app:tint="@color/error" />

    </LinearLayout>
</com.google.android.material.card.MaterialCardView>
"""

dialog_add_category = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="24dp">

    <TextView
        android:id="@+id/tvDialogTitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Add Category"
        android:textSize="20sp"
        android:textStyle="bold"
        android:layout_marginBottom="16dp" />

    <ImageView
        android:id="@+id/ivSelectImage"
        android:layout_width="120dp"
        android:layout_height="120dp"
        android:layout_gravity="center"
        android:layout_marginBottom="16dp"
        android:background="#EEEEEE"
        android:scaleType="centerCrop"
        android:src="@android:drawable/ic_menu_camera" />

    <EditText
        android:id="@+id/etCategoryName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Category Name"
        android:inputType="text"
        android:layout_marginBottom="24dp" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:gravity="end">

        <Button
            android:id="@+id/btnCancel"
            style="@style/Widget.MaterialComponents.Button.TextButton"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Cancel" />

        <Button
            android:id="@+id/btnSave"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Save"
            android:layout_marginStart="8dp" />
    </LinearLayout>
</LinearLayout>
"""

# Kotlin Code
category_model = """package com.example.adminapp.models

data class Category(
    var categoryId: String = "",
    var categoryName: String = "",
    var categoryImage: String = "",
    var createdAt: Long = 0
)
"""

category_adapter = """package com.example.adminapp.adapters

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
"""

category_activity = """package com.example.adminapp

import android.app.Dialog
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.View
import android.view.Window
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.bumptech.glide.Glide
import com.example.adminapp.adapters.CategoryAdapter
import com.example.adminapp.databinding.ActivityCategoryBinding
import com.example.adminapp.models.Category
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.storage.FirebaseStorage
import java.util.*

class CategoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityCategoryBinding
    private lateinit var firestore: FirebaseFirestore
    private lateinit var storage: FirebaseStorage
    private lateinit var adapter: CategoryAdapter
    private var categoryList = mutableListOf<Category>()
    
    private var imageUri: Uri? = null
    private var dialogImageView: ImageView? = null

    private val selectImageLauncher = registerForActivityResult(ActivityResultContracts.GetContent()) { uri: Uri? ->
        uri?.let {
            imageUri = it
            dialogImageView?.setImageURI(it)
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCategoryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        firestore = FirebaseFirestore.getInstance()
        storage = FirebaseStorage.getInstance()

        binding.toolbar.setNavigationIcon(androidx.appcompat.R.drawable.abc_ic_ab_back_material)
        binding.toolbar.setNavigationOnClickListener { finish() }

        setupRecyclerView()
        loadCategories()

        binding.fabAdd.setOnClickListener {
            showAddEditDialog(null)
        }
    }

    private fun setupRecyclerView() {
        adapter = CategoryAdapter(categoryList, { category ->
            showAddEditDialog(category)
        }, { category ->
            showDeleteDialog(category)
        })
        binding.recyclerView.layoutManager = LinearLayoutManager(this)
        binding.recyclerView.adapter = adapter
    }

    private fun loadCategories() {
        binding.progressBar.visibility = View.VISIBLE
        firestore.collection("categories").addSnapshotListener { snapshot, error ->
            binding.progressBar.visibility = View.GONE
            if (error != null) {
                Toast.makeText(this, "Failed to load: ${error.message}", Toast.LENGTH_SHORT).show()
                return@addSnapshotListener
            }
            
            categoryList.clear()
            snapshot?.let {
                for (doc in it) {
                    val category = doc.toObject(Category::class.java)
                    categoryList.add(category)
                }
            }
            
            if (categoryList.isEmpty()) {
                binding.tvEmpty.visibility = View.VISIBLE
            } else {
                binding.tvEmpty.visibility = View.GONE
            }
            
            adapter.updateList(categoryList)
        }
    }

    private fun showAddEditDialog(category: Category?) {
        imageUri = null
        val dialog = Dialog(this)
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE)
        dialog.setContentView(R.layout.dialog_add_category)
        dialog.window?.setLayout(android.view.ViewGroup.LayoutParams.MATCH_PARENT, android.view.ViewGroup.LayoutParams.WRAP_CONTENT)

        val tvTitle = dialog.findViewById<TextView>(R.id.tvDialogTitle)
        val ivSelectImage = dialog.findViewById<ImageView>(R.id.ivSelectImage)
        val etCategoryName = dialog.findViewById<EditText>(R.id.etCategoryName)
        val btnSave = dialog.findViewById<Button>(R.id.btnSave)
        val btnCancel = dialog.findViewById<Button>(R.id.btnCancel)

        dialogImageView = ivSelectImage

        if (category != null) {
            tvTitle.text = "Edit Category"
            etCategoryName.setText(category.categoryName)
            Glide.with(this).load(category.categoryImage).into(ivSelectImage)
        }

        ivSelectImage.setOnClickListener {
            selectImageLauncher.launch("image/*")
        }

        btnCancel.setOnClickListener { dialog.dismiss() }

        btnSave.setOnClickListener {
            val name = etCategoryName.text.toString().trim()
            if (name.isEmpty()) {
                Toast.makeText(this, "Category name is required", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            if (category == null && imageUri == null) {
                Toast.makeText(this, "Image is required", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            dialog.dismiss()
            binding.progressBar.visibility = View.VISIBLE

            if (imageUri != null) {
                uploadImageAndSaveCategory(category, name)
            } else {
                // Updating without changing image
                updateCategory(category!!, name, category.categoryImage)
            }
        }

        dialog.show()
    }

    private fun uploadImageAndSaveCategory(category: Category?, name: String) {
        val fileName = UUID.randomUUID().toString() + ".jpg"
        val ref = storage.reference.child("category_images/$fileName")
        
        ref.putFile(imageUri!!)
            .addOnSuccessListener {
                ref.downloadUrl.addOnSuccessListener { uri ->
                    if (category == null) {
                        saveNewCategory(name, uri.toString())
                    } else {
                        updateCategory(category, name, uri.toString())
                    }
                }
            }
            .addOnFailureListener { e ->
                binding.progressBar.visibility = View.GONE
                Toast.makeText(this, "Upload failed: ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    private fun saveNewCategory(name: String, imageUrl: String) {
        val id = firestore.collection("categories").document().id
        val category = Category(id, name, imageUrl, System.currentTimeMillis())
        
        firestore.collection("categories").document(id).set(category)
            .addOnSuccessListener {
                binding.progressBar.visibility = View.GONE
                Toast.makeText(this, "Category Added Successfully", Toast.LENGTH_SHORT).show()
            }
            .addOnFailureListener { e ->
                binding.progressBar.visibility = View.GONE
                Toast.makeText(this, "Failed to save: ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    private fun updateCategory(category: Category, name: String, imageUrl: String) {
        val updates = mapOf(
            "categoryName" to name,
            "categoryImage" to imageUrl
        )
        
        firestore.collection("categories").document(category.categoryId).update(updates)
            .addOnSuccessListener {
                binding.progressBar.visibility = View.GONE
                Toast.makeText(this, "Category Updated Successfully", Toast.LENGTH_SHORT).show()
            }
            .addOnFailureListener { e ->
                binding.progressBar.visibility = View.GONE
                Toast.makeText(this, "Failed to update: ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    private fun showDeleteDialog(category: Category) {
        AlertDialog.Builder(this)
            .setTitle("Delete Category")
            .setMessage("Are you sure you want to delete this category?")
            .setPositiveButton("Yes") { _, _ ->
                binding.progressBar.visibility = View.VISIBLE
                firestore.collection("categories").document(category.categoryId).delete()
                    .addOnSuccessListener {
                        // Optionally delete image from storage
                        try {
                            storage.getReferenceFromUrl(category.categoryImage).delete()
                        } catch (e: Exception) {}
                        
                        binding.progressBar.visibility = View.GONE
                        Toast.makeText(this, "Category Deleted Successfully", Toast.LENGTH_SHORT).show()
                    }
                    .addOnFailureListener { e ->
                        binding.progressBar.visibility = View.GONE
                        Toast.makeText(this, "Delete failed: ${e.message}", Toast.LENGTH_SHORT).show()
                    }
            }
            .setNegativeButton("No", null)
            .show()
    }
}
"""

with open(os.path.join(res_layout, "activity_category.xml"), "w") as f: f.write(activity_category)
with open(os.path.join(res_layout, "item_category.xml"), "w") as f: f.write(item_category)
with open(os.path.join(res_layout, "dialog_add_category.xml"), "w") as f: f.write(dialog_add_category)

with open(os.path.join(models_dir, "Category.kt"), "w") as f: f.write(category_model)
with open(os.path.join(adapters_dir, "CategoryAdapter.kt"), "w") as f: f.write(category_adapter)
with open(os.path.join(java_dir, "CategoryActivity.kt"), "w") as f: f.write(category_activity)

print("Category module generated.")
