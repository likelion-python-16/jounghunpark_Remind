const axiosInstance = axios.create({
    baseURL: '/',
    headers: {
        "X-CSRFToken":getCookie("csrftoken"),
        // "Content-Type":"application/json"
        "Content-Type": "multipart/form-data"
    }
});



// 전역에서 사용할 수 있도록 등록
window.axiosInstance = axiosInstance;