class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }
  watch() {
    console.log(`${this.uploader} watched all ${this.time} sec of ${this.title}!`);
  }
}

const video1 = new Video("Funny Clips", "Amit", 200);
video1.watch();
const video2 = new Video("Summer fun", "Michal", 120);
video2.watch();

const videoData = [
    {
        title : 'happy',
        uploader : 'Tom',
        time : 60
    },
    {
        title : 'New York',
        uploader : 'Shula',
        time : 75
    },
    {
        title : 'Schroon Lake',
        uploader : 'Kfir',
        time : 80
    },
    {
        title : 'Grandparents',
        uploader : 'Gilat',
        time : 200
    },
    {
        title : 'Family time',
        uploader : 'Rami',
        time : 300
    }
]

videoData.forEach((data) => {
    const{title, uploader, time} = data;
    const videoInstance = new Video(title, uploader, time);
    videoInstance.watch();
})