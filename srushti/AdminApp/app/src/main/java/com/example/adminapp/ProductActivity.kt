package com.example.adminapp

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
