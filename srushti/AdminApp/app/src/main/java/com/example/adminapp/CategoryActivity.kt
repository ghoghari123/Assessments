package com.example.adminapp

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
