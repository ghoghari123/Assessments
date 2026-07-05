package com.example.adminapp

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.SearchView
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.adminapp.adapters.UserAdapter
import com.example.adminapp.databinding.ActivityUserBinding
import com.example.adminapp.models.User
import com.google.firebase.firestore.FirebaseFirestore
import java.util.*

class UserActivity : AppCompatActivity() {

    private lateinit var binding: ActivityUserBinding
    private lateinit var firestore: FirebaseFirestore
    private lateinit var adapter: UserAdapter
    
    private var userList = mutableListOf<User>()
    private var filteredList = mutableListOf<User>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityUserBinding.inflate(layoutInflater)
        setContentView(binding.root)

        firestore = FirebaseFirestore.getInstance()

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        setupRecyclerView()
        loadUsers()
    }

    private fun setupRecyclerView() {
        adapter = UserAdapter(filteredList, { user ->
            val intent = Intent(this, UserDetailsActivity::class.java)
            intent.putExtra("USER_ID", user.userId)
            startActivity(intent)
        }, { user ->
            toggleUserStatus(user)
        })
        binding.recyclerView.layoutManager = LinearLayoutManager(this)
        binding.recyclerView.adapter = adapter
    }

    private fun loadUsers() {
        binding.progressBar.visibility = View.VISIBLE
        firestore.collection("users").whereEqualTo("role", "User").addSnapshotListener { snapshot, error ->
            binding.progressBar.visibility = View.GONE
            if (error != null) {
                Toast.makeText(this, "Failed to load: ${error.message}", Toast.LENGTH_SHORT).show()
                return@addSnapshotListener
            }
            
            userList.clear()
            snapshot?.let {
                for (doc in it) {
                    val user = doc.toObject(User::class.java)
                    user.userId = doc.id
                    userList.add(user)
                }
            }
            filterList("")
        }
    }

    private fun filterList(query: String) {
        filteredList.clear()
        if (query.isEmpty()) {
            filteredList.addAll(userList)
        } else {
            val lowerCaseQuery = query.lowercase(Locale.getDefault())
            for (user in userList) {
                if (user.fullName.lowercase(Locale.getDefault()).contains(lowerCaseQuery) ||
                    user.email.lowercase(Locale.getDefault()).contains(lowerCaseQuery) ||
                    user.mobile.contains(lowerCaseQuery)) {
                    filteredList.add(user)
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
                filterList(newText ?: "")
                return true
            }
        })
        return super.onPrepareOptionsMenu(menu)
    }

    private fun toggleUserStatus(user: User) {
        val newStatus = if (user.status == "Blocked") "Active" else "Blocked"
        val message = if (newStatus == "Blocked") "Are you sure you want to block this user?" else "Are you sure you want to unblock this user?"
        
        AlertDialog.Builder(this)
            .setTitle("$newStatus User")
            .setMessage(message)
            .setPositiveButton("Yes") { _, _ ->
                binding.progressBar.visibility = View.VISIBLE
                firestore.collection("users").document(user.userId).update("status", newStatus)
                    .addOnSuccessListener {
                        binding.progressBar.visibility = View.GONE
                        Toast.makeText(this, "User $newStatus Successfully", Toast.LENGTH_SHORT).show()
                    }
                    .addOnFailureListener { e ->
                        binding.progressBar.visibility = View.GONE
                        Toast.makeText(this, "Failed: ${e.message}", Toast.LENGTH_SHORT).show()
                    }
            }
            .setNegativeButton("No", null)
            .show()
    }
}
