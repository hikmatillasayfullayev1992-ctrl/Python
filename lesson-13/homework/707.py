{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5b73dfd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import date, datetime\n",
    "\n",
    "dob_str = input(\"Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): \")\n",
    "dob = datetime.strptime(dob_str, \"%Y-%m-%d\").date()\n",
    "today = date.today()\n",
    "\n",
    "years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))\n",
    "months = (today.year - dob.year) * 12 + today.month - dob.month\n",
    "days = (today - dob).days\n",
    "\n",
    "print(f\"Sizning yoshingiz: {years} yil, {months} oy, {days} kun\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0d30539",
   "metadata": {},
   "outputs": [],
   "source": [
    "dob_str = input(\"Tug‘ilgan kuningiz (YYYY-MM-DD): \")\n",
    "dob = datetime.strptime(dob_str, \"%Y-%m-%d\").date()\n",
    "today = date.today()\n",
    "\n",
    "next_birthday = dob.replace(year=today.year)\n",
    "if next_birthday < today:\n",
    "    next_birthday = next_birthday.replace(year=today.year + 1)\n",
    "\n",
    "days_left = (next_birthday - today).days\n",
    "print(f\"Keyingi tug‘ilgan kuningizga {days_left} kun qoldi 🎉\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "accf521f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import timedelta\n",
    "\n",
    "now_str = input(\"Hozirgi sana va vaqt (YYYY-MM-DD HH:MM): \")\n",
    "now = datetime.strptime(now_str, \"%Y-%m-%d %H:%M\")\n",
    "\n",
    "hours = int(input(\"Uchrashuv davomiyligi (soat): \"))\n",
    "minutes = int(input(\"Uchrashuv davomiyligi (daqiqa): \"))\n",
    "\n",
    "end_time = now + timedelta(hours=hours, minutes=minutes)\n",
    "print(\"Uchrashuv tugash vaqti:\", end_time)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce58314d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "import pytz\n",
    "\n",
    "dt_str = input(\"Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): \")\n",
    "from_zone = input(\"Hozirgi timezone (masalan, Asia/Tashkent): \")\n",
    "to_zone = input(\"Qaysi timezone ga o‘tkazilsin?: \")\n",
    "\n",
    "dt = datetime.strptime(dt_str, \"%Y-%m-%d %H:%M\")\n",
    "from_tz = pytz.timezone(from_zone)\n",
    "to_tz = pytz.timezone(to_zone)\n",
    "\n",
    "dt_local = from_tz.localize(dt)\n",
    "dt_converted = dt_local.astimezone(to_tz)\n",
    "\n",
    "print(\"Natija:\", dt_converted.strftime(\"%Y-%m-%d %H:%M\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5adf2096",
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "\n",
    "future_str = input(\"Kelajakdagi sana va vaqt (YYYY-MM-DD HH:MM:SS): \")\n",
    "future = datetime.strptime(future_str, \"%Y-%m-%d %H:%M:%S\")\n",
    "\n",
    "while True:\n",
    "    now = datetime.now()\n",
    "    if now >= future:\n",
    "        print(\"⏰ Vaqt tugadi!\")\n",
    "        break\n",
    "    remaining = future - now\n",
    "    print(\"Qolgan vaqt:\", remaining, end=\"\\r\")\n",
    "    time.sleep(1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc89e0eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "\n",
    "email = input(\"Emailni kiriting: \")\n",
    "pattern = r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$'\n",
    "\n",
    "if re.match(pattern, email):\n",
    "    print(\"✅ To‘g‘ri email manzil\")\n",
    "else:\n",
    "    print(\"❌ Noto‘g‘ri email manzil\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4d2b061",
   "metadata": {},
   "outputs": [],
   "source": [
    "num = input(\"Telefon raqam kiriting (faqat raqamlar): \")\n",
    "\n",
    "if len(num) == 10 and num.isdigit():\n",
    "    formatted = f\"({num[:3]}) {num[3:6]}-{num[6:]}\"\n",
    "    print(\"Formatlangan raqam:\", formatted)\n",
    "else:\n",
    "    print(\"❌ 10 ta raqam kiriting\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6da6bc1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "\n",
    "password = input(\"Parolni kiriting: \")\n",
    "\n",
    "if (len(password) >= 8 and\n",
    "    re.search(r'[A-Z]', password) and\n",
    "    re.search(r'[a-z]', password) and\n",
    "    re.search(r'[0-9]', password)):\n",
    "    print(\"✅ Kuchli parol\")\n",
    "else:\n",
    "    print(\"❌ Parol kuchsiz (kamida 8 belgidan iborat, katta-harflar, kichik-harflar va raqam bo‘lishi kerak)\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81e2a115",
   "metadata": {},
   "outputs": [],
   "source": [
    "text = \"Python is powerful. Python is easy to learn. Python is everywhere.\"\n",
    "word = input(\"Qidiriladigan so‘z: \")\n",
    "\n",
    "positions = [i for i in range(len(text.split())) if text.split()[i].lower() == word.lower()]\n",
    "print(f\"'{word}' so‘zi {len(positions)} marta topildi. Indekslar:\", positions)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f2ade54",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "\n",
    "text = input(\"Matn kiriting (masalan: Today is 2025-09-10, tomorrow is 2025/09/11): \")\n",
    "dates = re.findall(r'\\d{4}[-/]\\d{2}[-/]\\d{2}', text)\n",
    "\n",
    "print(\"Topilgan sanalar:\", dates)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
