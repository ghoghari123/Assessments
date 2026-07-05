import os

res_layout = "f:/srushti/AdminApp/app/src/main/res/layout"
java_dir = "f:/srushti/AdminApp/app/src/main/java/com/example/adminapp"
models_dir = os.path.join(java_dir, "models")
adapters_dir = os.path.join(java_dir, "adapters")

# Layouts
activity_product = """<?xml version="1.0" encoding="utf-8"?>
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
            app:title="Manage Products"
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
        android:text="No Products Found"
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

item_product = """<?xml version="1.0" encoding="utf-8"?>
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
        android:padding="12dp">

        <ImageView
            android:id="@+id/ivProduct"
            android:layout_width="80dp"
            android:layout_height="80dp"
            android:scaleType="centerCrop"
            android:background="#EEEEEE" />

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:layout_marginStart="12dp"
            android:orientation="vertical">

            <TextView
                android:id="@+id/tvProductName"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="16sp"
                android:textStyle="bold"
                android:textColor="@color/black" />

            <TextView
                android:id="@+id/tvCategoryName"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="14sp"
                android:textColor="@color/gray" />

            <TextView
                android:id="@+id/tvPriceInfo"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="14sp"
                android:textColor="@color/primary"
                android:textStyle="bold" />

            <TextView
                android:id="@+id/tvStock"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="12sp"
                android:textColor="@color/gray" />
        </LinearLayout>

        <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="match_parent"
            android:orientation="vertical"
            android:gravity="center">

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
                android:layout_marginTop="8dp"
                android:background="?attr/selectableItemBackgroundBorderless"
                android:src="@android:drawable/ic_menu_delete"
                app:tint="@color/error" />
        </LinearLayout>

    </LinearLayout>
</com.google.android.material.card.MaterialCardView>
"""

dialog_add_product = """<?xml version="1.0" encoding="utf-8"?>
<androidx.core.widget.NestedScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:padding="24dp">
    
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/tvDialogTitle"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Add Product"
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
            android:id="@+id/etProductName"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Product Name"
            android:inputType="text"
            android:layout_marginBottom="12dp" />

        <Spinner
            android:id="@+id/spinnerCategory"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="12dp" />

        <EditText
            android:id="@+id/etDescription"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Description"
            android:inputType="textMultiLine"
            android:lines="3"
            android:layout_marginBottom="12dp" />

        <EditText
            android:id="@+id/etOriginalPrice"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Original Price"
            android:inputType="numberDecimal"
            android:layout_marginBottom="12dp" />

        <EditText
            android:id="@+id/etDiscount"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Discount (%)"
            android:inputType="numberDecimal"
            android:layout_marginBottom="12dp" />

        <EditText
            android:id="@+id/etStock"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Stock Quantity"
            android:inputType="number"
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
</androidx.core.widget.NestedScrollView>
"""

# Kotlin Code
product_model = """package com.example.adminapp.models

data class Product(
    var productId: String = "",
    var productName: String = "",
    var categoryId: String = "",
    var categoryName: String = "",
    var description: String = "",
    var originalPrice: Double = 0.0,
    var discount: Double = 0.0,
    var finalPrice: Double = 0.0,
    var stock: Int = 0,
    var productImage: String = "",
    var createdAt: Long = 0
)
"""

product_adapter = """package com.example.adminapp.adapters

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
"""

product_activity = """package com.example.adminapp

import android.app.Dialog
import android.net.Uri
import android.os.Bundle
import android.view.Menu
import android.view.View
import android.view.Window
import android.widget.*
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.SearchView
import androidx.recyclerview.widget.LinearLayoutManager
import com.bumptech.glide.Glide
import com.example.adminapp.adapters.ProductAdapter
import com.example.adminapp.databinding.ActivityProductBinding
import com.example.adminapp.models.Category
import com.example.adminapp.models.Product
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.storage.FirebaseStorage
import java.util.*

class ProductActivity : AppCompatActivity() {

    private lateinit var binding: ActivityProductBinding
    private lateinit var firestore: FirebaseFirestore
    private lateinit var storage: FirebaseStorage
    private lateinit var adapter: ProductAdapter
    
    private var productList = mutableListOf<Product>()
    private var filteredList = mutableListOf<Product>()
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
        binding = ActivityProductBinding.inflate(layoutInflater)
        setContentView(binding.root)

        firestore = FirebaseFirestore.getInstance()
        storage = FirebaseStorage.getInstance()

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        setupRecyclerView()
        loadCategories()
        loadProducts()

        binding.fabAdd.setOnClickListener {
            if (categoryList.isEmpty()) {
                Toast.makeText(this, "Please add a category first", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            showAddEditDialog(null)
        }
    }

    private fun setupRecyclerView() {
        adapter = ProductAdapter(filteredList, { product ->
            showAddEditDialog(product)
        }, { product ->
            showDeleteDialog(product)
        })
        binding.recyclerView.layoutManager = LinearLayoutManager(this)
        binding.recyclerView.adapter = adapter
    }

    private fun loadCategories() {
        firestore.collection("categories").get().addOnSuccessListener { snapshot ->
            categoryList.clear()
            for (doc in snapshot) {
                categoryList.add(doc.toObject(Category::class.java))
            }
        }
    }

    private fun loadProducts() {
        binding.progressBar.visibility = View.VISIBLE
        firestore.collection("products").addSnapshotListener { snapshot, error ->
            binding.progressBar.visibility = View.GONE
            if (error != null) {
                Toast.makeText(this, "Failed to load: ${error.message}", Toast.LENGTH_SHORT).show()
                return@addSnapshotListener
            }
            
            productList.clear()
            snapshot?.let {
                for (doc in it) {
                    productList.add(doc.toObject(Product::class.java))
                }
            }
            
            filterList("")
        }
    }

    private fun filterList(query: String) {
        filteredList.clear()
        if (query.isEmpty()) {
            filteredList.addAll(productList)
        } else {
            val lowerCaseQuery = query.lowercase(Locale.getDefault())
            for (product in productList) {
                if (product.productName.lowercase(Locale.getDefault()).contains(lowerCaseQuery) ||
                    product.categoryName.lowercase(Locale.getDefault()).contains(lowerCaseQuery)) {
                    filteredList.add(product)
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

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(androidx.appcompat.R.menu.abc_search_view, menu)
        val searchItem = menu.findItem(androidx.appcompat.R.id.search_go_btn) // Using system ID
        // Actually to add SearchView properly, we should create a res/menu/search_menu.xml
        // For simplicity, we just dynamically add it here
        return true
    }
    
    // Better way to add SearchView programmatically for the script
    override fun onPrepareOptionsMenu(menu: Menu?): Boolean {
        menu?.clear()
        val searchItem = menu?.add(Menu.NONE, 1001, Menu.NONE, "Search")
        searchItem?.setIcon(android.R.drawable.ic_menu_search)
        searchItem?.setShowAsAction(Menu.SHOW_AS_ACTION_ALWAYS or Menu.SHOW_AS_ACTION_COLLAPSE_ACTION_VIEW)
        val searchView = SearchView(this)
        searchItem?.actionView = searchView
        
        searchView.setOnQueryTextListener(object : SearchView.OnQueryTextListener {
            override fun onQueryTextSubmit(query: String?): Boolean {
                return false
            }
            override fun onQueryTextChange(newText: String?): Boolean {
                filterList(newText ?: "")
                return true
            }
        })
        return super.onPrepareOptionsMenu(menu)
    }

    private fun showAddEditDialog(product: Product?) {
        imageUri = null
        val dialog = Dialog(this)
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE)
        dialog.setContentView(R.layout.dialog_add_product)
        dialog.window?.setLayout(android.view.ViewGroup.LayoutParams.MATCH_PARENT, android.view.ViewGroup.LayoutParams.WRAP_CONTENT)

        val tvTitle = dialog.findViewById<TextView>(R.id.tvDialogTitle)
        val ivSelectImage = dialog.findViewById<ImageView>(R.id.ivSelectImage)
        val etProductName = dialog.findViewById<EditText>(R.id.etProductName)
        val spinnerCategory = dialog.findViewById<Spinner>(R.id.spinnerCategory)
        val etDescription = dialog.findViewById<EditText>(R.id.etDescription)
        val etOriginalPrice = dialog.findViewById<EditText>(R.id.etOriginalPrice)
        val etDiscount = dialog.findViewById<EditText>(R.id.etDiscount)
        val etStock = dialog.findViewById<EditText>(R.id.etStock)
        val btnSave = dialog.findViewById<Button>(R.id.btnSave)
        val btnCancel = dialog.findViewById<Button>(R.id.btnCancel)

        dialogImageView = ivSelectImage
        
        val categoryNames = categoryList.map { it.categoryName }
        val spinnerAdapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, categoryNames)
        spinnerCategory.adapter = spinnerAdapter

        if (product != null) {
            tvTitle.text = "Edit Product"
            etProductName.setText(product.productName)
            etDescription.setText(product.description)
            etOriginalPrice.setText(product.originalPrice.toString())
            etDiscount.setText(product.discount.toString())
            etStock.setText(product.stock.toString())
            
            val spinnerPos = categoryNames.indexOf(product.categoryName)
            if (spinnerPos >= 0) spinnerCategory.setSelection(spinnerPos)
            
            Glide.with(this).load(product.productImage).into(ivSelectImage)
        }

        ivSelectImage.setOnClickListener {
            selectImageLauncher.launch("image/*")
        }

        btnCancel.setOnClickListener { dialog.dismiss() }

        btnSave.setOnClickListener {
            val name = etProductName.text.toString().trim()
            val desc = etDescription.text.toString().trim()
            val origPriceStr = etOriginalPrice.text.toString().trim()
            val discountStr = etDiscount.text.toString().trim()
            val stockStr = etStock.text.toString().trim()
            
            if (name.isEmpty() || desc.isEmpty() || origPriceStr.isEmpty() || discountStr.isEmpty() || stockStr.isEmpty()) {
                Toast.makeText(this, "All fields are required", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            
            val origPrice = origPriceStr.toDoubleOrNull() ?: 0.0
            val discount = discountStr.toDoubleOrNull() ?: 0.0
            val stock = stockStr.toIntOrNull() ?: 0
            
            if (origPrice <= 0 || discount < 0 || stock < 0) {
                Toast.makeText(this, "Invalid number inputs", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            if (product == null && imageUri == null) {
                Toast.makeText(this, "Image is required", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            
            val selectedCategory = categoryList[spinnerCategory.selectedItemPosition]
            val finalPrice = origPrice - (origPrice * discount / 100)

            dialog.dismiss()
            binding.progressBar.visibility = View.VISIBLE

            val pData = Product(
                productId = product?.productId ?: "",
                productName = name,
                categoryId = selectedCategory.categoryId,
                categoryName = selectedCategory.categoryName,
                description = desc,
                originalPrice = origPrice,
                discount = discount,
                finalPrice = finalPrice,
                stock = stock,
                productImage = product?.productImage ?: "",
                createdAt = product?.createdAt ?: System.currentTimeMillis()
            )

            if (imageUri != null) {
                uploadImageAndSaveProduct(pData)
            } else {
                saveProductData(pData)
            }
        }

        dialog.show()
    }

    private fun uploadImageAndSaveProduct(product: Product) {
        val fileName = UUID.randomUUID().toString() + ".jpg"
        val ref = storage.reference.child("product_images/$fileName")
        
        ref.putFile(imageUri!!)
            .addOnSuccessListener {
                ref.downloadUrl.addOnSuccessListener { uri ->
                    product.productImage = uri.toString()
                    saveProductData(product)
                }
            }
            .addOnFailureListener { e ->
                binding.progressBar.visibility = View.GONE
                Toast.makeText(this, "Upload failed: ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    private fun saveProductData(product: Product) {
        if (product.productId.isEmpty()) {
            product.productId = firestore.collection("products").document().id
        }
        
        firestore.collection("products").document(product.productId).set(product)
            .addOnSuccessListener {
                binding.progressBar.visibility = View.GONE
                Toast.makeText(this, "Product Saved Successfully", Toast.LENGTH_SHORT).show()
            }
            .addOnFailureListener { e ->
                binding.progressBar.visibility = View.GONE
                Toast.makeText(this, "Failed to save: ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    private fun showDeleteDialog(product: Product) {
        AlertDialog.Builder(this)
            .setTitle("Delete Product")
            .setMessage("Are you sure you want to delete this product?")
            .setPositiveButton("Yes") { _, _ ->
                binding.progressBar.visibility = View.VISIBLE
                firestore.collection("products").document(product.productId).delete()
                    .addOnSuccessListener {
                        try {
                            storage.getReferenceFromUrl(product.productImage).delete()
                        } catch (e: Exception) {}
                        binding.progressBar.visibility = View.GONE
                        Toast.makeText(this, "Product Deleted Successfully", Toast.LENGTH_SHORT).show()
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

with open(os.path.join(res_layout, "activity_product.xml"), "w", encoding="utf-8") as f: f.write(activity_product)
with open(os.path.join(res_layout, "item_product.xml"), "w", encoding="utf-8") as f: f.write(item_product)
with open(os.path.join(res_layout, "dialog_add_product.xml"), "w", encoding="utf-8") as f: f.write(dialog_add_product)

with open(os.path.join(models_dir, "Product.kt"), "w", encoding="utf-8") as f: f.write(product_model)
with open(os.path.join(adapters_dir, "ProductAdapter.kt"), "w", encoding="utf-8") as f: f.write(product_adapter)
with open(os.path.join(java_dir, "ProductActivity.kt"), "w", encoding="utf-8") as f: f.write(product_activity)

print("Product module generated.")
