document.addEventListener('DOMContentLoaded', function() {
    const playerImage = document.getElementById('player-image');

    if (playerImage) {
        console.log('GIF 元素加載成功');
        playerImage.addEventListener('click', () => {
            console.log('GIF 被點擊');
            playerImage.classList.add('hidden');

            setTimeout(() => {
                window.location.href = '/livingroom';
            }, 1500);
        });
    } else {
        console.error('找不到 GIF 元素');
    }
});
