class User < ActiveRecord::Base
  attr_accessible :first_name, :last_name, :email, :password
  has_and_belongs_to_many :projects
  has_many :tickets

  validates_presence_of :first_name, :last_name, :email, :password
  validates :first_name,
            :length => { :minimum => 2, :maximum => 20 }

  validates :last_name,
            :length => { :minimum => 2, :maximum => 20 }

  validates_format_of :email, 
                      :with => /^(|(([A-Za-z0-9]+_+)|([A-Za-z0-9]+\-+)|([A-Za-z0-9]+\.+)|([A-Za-z0-9]+\++))*[A-Za-z0-9]+@((\w+\-+)|(\w+\.))*\w{1,63}\.[a-zA-Z]{2,6})$/i
end