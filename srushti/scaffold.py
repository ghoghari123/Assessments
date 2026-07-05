import os

project_dir = "f:/srushti/AdminApp"
app_dir = os.path.join(project_dir, "app")
src_main = os.path.join(app_dir, "src/main")
java_dir = os.path.join(src_main, "java/com/example/adminapp")
res_dir = os.path.join(src_main, "res")

# Directories to create
dirs = [
    java_dir,
    os.path.join(java_dir, "models"),
    os.path.join(java_dir, "adapters"),
    os.path.join(java_dir, "utils"),
    os.path.join(res_dir, "layout"),
    os.path.join(res_dir, "values"),
    os.path.join(res_dir, "drawable"),
    os.path.join(res_dir, "menu"),
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

# Basic Gradle files
with open(os.path.join(project_dir, "build.gradle"), "w") as f:
    f.write("""// Top-level build file
buildscript {
    ext.kotlin_version = "1.9.0"
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:8.1.1'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
        classpath 'com.google.gms:google-services:4.4.0'
    }
}
task clean(type: Delete) {
    delete rootProject.buildDir
}
""")

with open(os.path.join(project_dir, "settings.gradle"), "w") as f:
    f.write("""pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "AdminApp"
include ':app'
""")

with open(os.path.join(project_dir, "gradle.properties"), "w") as f:
    f.write("""org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
android.enableJetifier=true
kotlin.code.style=official
""")

with open(os.path.join(app_dir, "build.gradle"), "w") as f:
    f.write("""plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
    id 'com.google.gms.google-services'
}

android {
    namespace 'com.example.adminapp'
    compileSdk 34

    defaultConfig {
        applicationId "com.example.adminapp"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = '17'
    }
    buildFeatures {
        viewBinding true
    }
}

dependencies {
    implementation 'androidx.core:core-ktx:1.12.0'
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.11.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
    
    // Firebase BoM
    implementation platform('com.google.firebase:firebase-bom:32.7.0')
    implementation 'com.google.firebase:firebase-analytics'
    implementation 'com.google.firebase:firebase-auth-ktx'
    implementation 'com.google.firebase:firebase-firestore-ktx'
    implementation 'com.google.firebase:firebase-storage-ktx'
    
    // Glide for image loading
    implementation 'com.github.bumptech.glide:glide:4.16.0'
    annotationProcessor 'com.github.bumptech.glide:compiler:4.16.0'
    
    // Circle ImageView
    implementation 'de.hdodenhof:circleimageview:3.1.0'
}
""")

with open(os.path.join(src_main, "AndroidManifest.xml"), "w") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.adminapp">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" android:maxSdkVersion="32"/>
    <uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.AdminApp">

        <activity
            android:name=".SplashActivity"
            android:exported="true"
            android:theme="@style/Theme.AdminApp.NoActionBar">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        
        <activity android:name=".LoginActivity" android:exported="false" android:theme="@style/Theme.AdminApp.NoActionBar"/>
        <activity android:name=".DashboardActivity" android:exported="false" android:theme="@style/Theme.AdminApp.NoActionBar"/>
        <activity android:name=".CategoryActivity" android:exported="false" android:theme="@style/Theme.AdminApp.NoActionBar"/>
        <activity android:name=".ProductActivity" android:exported="false" android:theme="@style/Theme.AdminApp.NoActionBar"/>
        <activity android:name=".UserActivity" android:exported="false" android:theme="@style/Theme.AdminApp.NoActionBar"/>
        <activity android:name=".UserDetailsActivity" android:exported="false" android:theme="@style/Theme.AdminApp.NoActionBar"/>
        <activity android:name=".OrderActivity" android:exported="false" android:theme="@style/Theme.AdminApp.NoActionBar"/>
        <activity android:name=".OrderDetailsActivity" android:exported="false" android:theme="@style/Theme.AdminApp.NoActionBar"/>

    </application>
</manifest>
""")

with open(os.path.join(res_dir, "values", "strings.xml"), "w") as f:
    f.write("""<resources>
    <string name="app_name">AdminApp</string>
</resources>
""")

with open(os.path.join(res_dir, "values", "colors.xml"), "w") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="primary">#4CAF50</color>
    <color name="primary_variant">#388E3C</color>
    <color name="secondary">#81C784</color>
    <color name="background">#F5F5F5</color>
    <color name="surface">#FFFFFF</color>
    <color name="error">#B00020</color>
    <color name="on_primary">#FFFFFF</color>
    <color name="on_secondary">#000000</color>
    <color name="on_background">#000000</color>
    <color name="on_surface">#000000</color>
    <color name="on_error">#FFFFFF</color>
    <color name="black">#FF000000</color>
    <color name="white">#FFFFFFFF</color>
    <color name="gray">#808080</color>
    <color name="light_gray">#E0E0E0</color>
</resources>
""")

with open(os.path.join(res_dir, "values", "themes.xml"), "w") as f:
    f.write("""<resources xmlns:tools="http://schemas.android.com/tools">
    <style name="Theme.AdminApp" parent="Theme.MaterialComponents.DayNight.DarkActionBar">
        <item name="colorPrimary">@color/primary</item>
        <item name="colorPrimaryVariant">@color/primary_variant</item>
        <item name="colorOnPrimary">@color/on_primary</item>
        <item name="colorSecondary">@color/secondary</item>
        <item name="colorSecondaryVariant">@color/primary</item>
        <item name="colorOnSecondary">@color/on_secondary</item>
        <item name="android:statusBarColor">?attr/colorPrimaryVariant</item>
    </style>

    <style name="Theme.AdminApp.NoActionBar">
        <item name="windowActionBar">false</item>
        <item name="windowNoTitle">true</item>
    </style>
</resources>
""")

print("Scaffolding complete.")
