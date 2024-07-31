def open_community_post(self):
        self.community_post_window = QMainWindow()
        self.community_post_window.setWindowTitle("Community Post(beta)")
        self.community_post_window.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.community_post_window.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        name_entry = QTextEdit()
        layout.addWidget(name_entry)

        post_text = QTextEdit()
        layout.addWidget(post_text)

        create_button = QPushButton("Create Post")
        create_button.clicked.connect(self.create_post)
        layout.addWidget(create_button)

        read_button = QPushButton("Read Post")
        read_button.clicked.connect(self.read_post)
        layout.addWidget(read_button)

        clear_button = QPushButton("Clear Fields")
        clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(clear_button)

        central_widget.setLayout(layout)

        self.community_post_window.show()
