package com.example.adminapp

import android.graphics.Color
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide
import com.example.adminapp.databinding.ActivityUserDetailsBinding
import com.example.adminapp.models.User
import com.google.firebase.firestore.FirebaseFirestore
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class UserDetailsActivity : AppCompatActivity() {

    private lateinit var binding: ActivityUserDetailsBinding
    private lateinit var firestore: FirebaseFirestore

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityUserDetailsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        firestore = FirebaseFirestore.getInstance()

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        val userId = intent.getStringExtra("USER_ID")
        if (userId != null) {
            loadUserDetails(userId)
        } else {
            Toast.makeText(this, "User ID missing", Toast.LENGTH_SHORT).show()
            finish()
        }
    }

    private fun loadUserDetails(userId: String) {
        firestore.collection("users").document(userId).get()
            .addOnSuccessListener { doc ->
                if (doc.exists()) {
                    val user = doc.toObject(User::class.java)
                    user?.let { displayUserDetails(it) }
                }
            }
            .addOnFailureListener { e ->
                Toast.makeText(this, "Error: ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    private fun displayUserDetails(user: User) {
        binding.tvDetName.text = "Name: ${user.fullName}"
        binding.tvDetEmail.text = "Email: ${user.email}"
        binding.tvDetMobile.text = "Mobile: ${user.mobile}"
        binding.tvDetGender.text = "Gender: ${if (user.gender.isEmpty()) "N/A" else user.gender}"
        binding.tvDetAddress.text = "Address: ${if (user.address.isEmpty()) "N/A" else user.address}"
        
        val sdf = SimpleDateFormat("dd MMM yyyy, HH:mm", Locale.getDefault())
        val dateStr = if (user.createdAt > 0) sdf.format(Date(user.createdAt)) else "N/A"
        binding.tvDetRegDate.text = "Registered: $dateStr"
        
        binding.tvDetOrders.text = "Total Orders: ${user.totalOrders}"
        
        binding.tvDetStatus.text = "Status: ${user.status}"
        if (user.status == "Blocked") {
            binding.tvDetStatus.setTextColor(Color.RED)
        } else {
            binding.tvDetStatus.setTextColor(Color.parseColor("#4CAF50"))
        }

        if (user.profileImage.isNotEmpty()) {
            Glide.with(this).load(user.profileImage).into(binding.ivProfileDetails)
        }
    }
}
