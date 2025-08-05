document.addEventListener('DOMContentLoaded', function () {
	const tabs = document.querySelectorAll('.tab');
	const contents = document.querySelectorAll('.tab-content');

	function activateTab(tabId) {
		// Убираем активность у всех
		tabs.forEach(t => t.classList.remove('active'));
		contents.forEach(c => c.classList.remove('active'));

		// Активируем нужные
		const activeTab = document.querySelector(`.tab[data-tab="${tabId}"]`);
		const content = document.getElementById('tab-' + tabId);

		if (!activeTab || !content) return;

		activeTab.classList.add('active');
		content.classList.add('active');

		// Заглушка
		content.innerHTML = '<p>Загрузка...</p>';

		// Подгружаем данные, если надо
		if (tabId === '1') {
			fetch('/last_active_deals/')
				.then(response => response.text())
				.then(html => {
					content.innerHTML = html;
				})
				.catch(() => {
					content.innerHTML = '<p>Ошибка загрузки данных.</p>';
				});
		}
	}

	// Навешиваем обработчики
	tabs.forEach(tab => {
		tab.addEventListener('click', () => {
			const tabId = tab.getAttribute('data-tab');
			activateTab(tabId);
		});
	});

	// Автоматически активируем первую вкладку при загрузке
	activateTab('1');
});
