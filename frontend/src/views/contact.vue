<template>
    <div class="container my-4 flex-grow-1">
      <!-- CONTACT US 標題 -->
  
      <!-- 聯絡資訊 -->
      <div class="contact-info d-flex flex-wrap justify-content-around text-center text-md-start mb-4">
        <div class="d-flex align-items-center mb-3">
          <i class="bi bi-clock-fill fs-4 me-2 text-warning"></i>
          <div>
            <div>週一至週五</div>
            <div>08:30 AM ~ 18:00 PM</div>
          </div>
        </div>
        <div class="d-flex align-items-center mb-3">
          <i class="bi bi-geo-alt-fill fs-4 me-2 text-warning"  @click="openMap" title="點擊可在地圖中查看位置"></i>
          <div>台中市潭子區中山路二段135號3樓</div>
        </div>
        <div class="d-flex align-items-center mb-3">
          <i class="bi bi-telephone-fill fs-4 me-2 text-warning"></i>
          <div>04-22388166</div>
        </div>
        <div class="d-flex align-items-center mb-3">
          <i class="bi bi-printer-fill fs-4 me-2 text-warning"></i>
          <div>04-22325377</div>
        </div>
        <div class="d-flex align-items-center mb-3">
          <i class="bi bi-envelope-fill fs-4 me-2 text-warning"></i>
          <div>cpck@ms22.hinet.net</div>
        </div>
        <div class="d-flex align-items-center mb-3">
          <i class="bi bi-phone-fill fs-4 me-2 text-warning"></i>
          <div>0930-215656</div>
        </div>
      </div>
  
      <!-- 聯絡表單 -->
      <form class="bg-light p-3 rounded shadow-sm">
        <h1 style="text-align: center;">聯絡表單</h1>
        <div class="mb-3">
          <label class="form-label">* 諮詢分類</label>
          <select class="form-select" required>
            <option value="">請選擇</option>
            <option value="general">一般諮詢</option>
            <option value="quote">報價詢問</option>
            <option value="other">其他</option>
          </select>
        </div>
  
        <div class="mb-3">
          <label class="form-label">* 姓名</label>
          <div class="input-group">
            <input type="text" class="form-control" required placeholder="請輸入姓名" />
            <div class="input-group-text">
              <input type="radio" name="gender" value="mr" class="form-check-input me-1" />
              先生
              <input type="radio" name="gender" value="ms" class="form-check-input ms-3 me-1" />
              小姐
            </div>
          </div>
        </div>
  
        <div class="mb-3">
          <label class="form-label">手機</label>
          <input type="tel" class="form-control" placeholder="09xx-xxx-xxx" />
        </div>
  
        <div class="mb-3">
          <label class="form-label">* 信箱</label>
          <input type="email" class="form-control" required placeholder="example@mail.com" />
        </div>
  
        <div class="mb-3">
          <label class="form-label">* 諮詢內容</label>
          <textarea class="form-control" rows="4" required></textarea>
        </div>
  
        <div class="text-end">
          <button type="submit" class="btn btn-warning rounded-circle">送出</button>
        </div>
      </form>
    </div>
  </template>
  
  <script setup>
  // 暫無邏輯
    function openMap() {
      const address = encodeURIComponent('台中市潭子区中山路二段135号')
      const url = `https://www.google.com/maps?q=${address}`
      window.open(url, '_blank')
    }
  </script>
  
  <style scoped>
  .input-group-text {
    background-color: #f8f9fa;
  }
  
  .contact-info i {
    min-width: 30px;
  }
  
  .contact-info > div {
    flex: 1 1 250px;
  }
  </style>
  