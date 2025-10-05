import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# تهيئة تطبيق فلاسك لخدمة الملفات الثابتة من مجلد "static"
app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# قائمة العيادات المحدثة بناءً على الجدول الجديد
CLINICS_LIST = """
"الباطنة-والجهاز-الهضمي-والكبد", "مسالك", "باطنة-عامة", "غدد-صماء-وسكر", "القلب-والإيكو",
"السونار-والدوبلكس", "جراحة-التجميل", "عظام", "جلدية-وليزر"
"""

# المسار الخاص بصفحة الموقع الرئيسية
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# تم حذف المسار الخاص بتوصية العيادات لأنه لم يعد مطلوباً

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
