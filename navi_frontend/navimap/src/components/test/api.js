const api = {
    harbor: {
        all(callback) {
            //  아직 백과 연결이 안되어 있으므로 가짜 데이터 사용
            const harbors = [
                {
                    seq: 1,
                    palce: "솔밭솔밥",
                    lat: 35.1886071,
                    lng: 126.8309932,
                },
                {
                    seq: 2,
                    palce: "이팅룸",
                    lat: 35.1882669,
                    lng: 126.8310951,
                },
                {
                    seq: 3,
                    palce: "유유샤브샤브",
                    lat: 35.1899379,
                    lng: 126.8306558,
                },
                {
                    seq: 4,
                    palce: "어트커피",
                    lat: 35.1891984,
                    lng: 126.8302127,
                },
                {
                    seq: 5,
                    palce: "필리아커피",
                    lat: 35.1890242,
                    lng: 126.8305266,
                },

            ]
            callback({ success: true, harbors})
        }
    }
}


export default api