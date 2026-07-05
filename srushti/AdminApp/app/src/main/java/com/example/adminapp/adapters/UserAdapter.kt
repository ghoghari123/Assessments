package com.example.adminapp.adapters

import android.graphics.Color
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.adminapp.R
import com.example.adminapp.models.User
import de.hdodenhof.circleimageview.CircleImageView
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class UserAdapter(
    private var userList: List<User>,
    private val onViewClick: (User) -> Unit,
    private val onBlockClick: (User) -> Unit
) : RecyclerView.Adapter<UserAdapter.UserViewHolder>() {

    class UserViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val ivProfile: CircleImageView = itemView.findViewById(R.id.ivProfile)
        val tvFullName: TextView = itemView.findViewById(R.id.tvFullName)
        val tvEmail: TextView = itemView.findViewById(R.id.tvEmail)
        val tvMobile: TextView = itemView.findViewById(R.id.tvMobile)
        val tvStatus: TextView = itemView.findViewById(R.id.tvStatus)
        val btnView: Button = itemView.findViewById(R.id.btnView)
        val btnBlock: Button = itemView.findViewById(R.id.btnBlock)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.id.item_user, parent, false)
        return UserViewHolder(view)
    }

    override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
        val user = userList[position]
        holder.tvFullName.text = user.fullName
        holder.tvEmail.text = user.email
        holder.tvMobile.text = user.mobile
        
        if (user.status == "Blocked") {
            holder.tvStatus.text = "Blocked"
            holder.tvStatus.setTextColor(Color.RED)
            holder.btnBlock.text = "Unblock"
            holder.btnBlock.setTextColor(Color.parseColor("#4CAF50"))
        } else {
            holder.tvStatus.text = "Active"
            holder.tvStatus.setTextColor(Color.parseColor("#4CAF50"))
            holder.btnBlock.text = "Block"
            holder.btnBlock.setTextColor(Color.RED)
        }
        
        if (user.profileImage.isNotEmpty()) {
            Glide.with(holder.itemView.context).load(user.profileImage).into(holder.ivProfile)
        } else {
            holder.ivProfile.setImageResource(R.mipmap.ic_launcher_round)
        }
        
        holder.btnView.setOnClickListener { onViewClick(user) }
        holder.btnBlock.setOnClickListener { onBlockClick(user) }
    }

    override fun getItemCount() = userList.size
    
    fun updateList(newList: List<User>) {
        userList = newList
        notifyDataSetChanged()
    }
}
